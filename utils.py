# utils.py
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import requests
import re

sentiment_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
embedding_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def analyze_text(text: str, lang: str) -> dict:
    sentiment = sentiment_model(text)[0]
    embedding = embedding_model.encode([text])[0]
    emoji = {
        "1 star": "😡 Πολύ αρνητικό",
        "2 stars": "🙁 Αρνητικό",
        "3 stars": "😐 Ουδέτερο",
        "4 stars": "🙂 Θετικό",
        "5 stars": "🤩 Πολύ θετικό"
    }.get(sentiment["label"], "🧐 Άγνωστο")

    emoji_result = f"### {emoji} (score: {sentiment['score']:.2f})"
    return {
        "emoji_result": emoji_result,
        "details": {
            "Συναίσθημα": sentiment["label"],
            "Embedding Vector (πρώτα 5)": embedding[:5].tolist(),
            "Μήκος Embedding": len(embedding)
        }
    }

def compare_texts(t1: str, t2: str) -> float:
    vecs = embedding_model.encode([t1, t2])
    return float(cosine_similarity([vecs[0]], [vecs[1]])[0][0])

def cluster_texts(texts: list, k: int = 2) -> dict:
    embeddings = embedding_model.encode(texts)
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    clusters = {i: [] for i in range(k)}
    for i, label in enumerate(labels):
        clusters[label].append(texts[i])
    return clusters

def extract_keywords(text: str, lang: str) -> list:
    tfidf = TfidfVectorizer(stop_words="english" if lang == "Αγγλικά" else None, max_features=10)
    tfidf_matrix = tfidf.fit_transform([text])
    words = tfidf.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    sorted_keywords = sorted(zip(words, scores), key=lambda x: x[1], reverse=True)
    return [w for w, s in sorted_keywords]

def fetch_reddit_posts(subreddit: str, limit: int = 10) -> list:
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {"User-agent": "TextLabBot 1.0"}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        posts = [post['data']['title'] for post in data['data']['children'] if 'title' in post['data']]
        return posts
    except Exception as e:
        return []
