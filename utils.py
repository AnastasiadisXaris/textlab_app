from transformers import pipeline
from sentence_transformers import SentenceTransformer
import numpy as np

# Προφόρτωση μοντέλων
sentiment_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
embedding_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def analyze_text(text: str) -> dict:
    sentiment = sentiment_model(text)[0]
    embedding = embedding_model.encode([text])[0]

    return {
        "Συναίσθημα": f"{sentiment['label']} (score: {sentiment['score']:.2f})",
        "Embedding Vector (πρώτα 5)": embedding[:5].tolist(),
        "Μήκος Embedding": len(embedding)
    }
