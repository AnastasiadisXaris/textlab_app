import streamlit as st
from utils import analyze_text, compare_texts, cluster_texts, extract_keywords

st.set_page_config(page_title="TextLab", layout="wide")
st.title("🔍 Ανάλυση κειμένου και Επεξεργασία Φυσικής Γλώσσας")

# Επιλογή γλώσσας
lang = st.radio("Επέλεξε γλώσσα κειμένου:", options=["Ελληνικά", "Αγγλικά"])

tab1, tab2, tab3, tab4 = st.tabs(["📄 Ανάλυση Κειμένου", "🆚 Σύγκριση", "🔗 Clustering", "🧠 Λέξεις-Κλειδιά"])

with tab1:
    text_input = st.text_area("Εισήγαγε κείμενο:", height=200)
    if st.button("Ανάλυση Κειμένου"):
        if text_input.strip():
            with st.spinner("🔎 Αναλύεται..."):
                result = analyze_text(text_input, lang=lang)
                st.subheader("📌 Αποτελέσματα:")
                st.markdown(result["emoji_result"])
                st.write(result["details"])
        else:
            st.warning("Παρακαλώ εισάγετε κείμενο πρώτα.")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        text1 = st.text_area("Κείμενο 1")
    with col2:
        text2 = st.text_area("Κείμενο 2")
    if st.button("Σύγκριση Κειμένων"):
        if text1 and text2:
            score = compare_texts(text1, text2)
            st.metric("Cosine Similarity", f"{score:.2f}")
        else:
            st.warning("Εισήγαγε και τα δύο κείμενα.")

with tab3:
    multi_input = st.text_area("Εισήγαγε πολλαπλά κείμενα (ένα ανά γραμμή):", height=200)
    if st.button("Clustering"):
        texts = [t.strip() for t in multi_input.split("\n") if t.strip()]
        if len(texts) >= 2:
            clusters = cluster_texts(texts)
            for i, group in clusters.items():
                st.markdown(f"**Cluster {i+1}:**")
                st.write(group)
        else:
            st.warning("Χρειάζονται τουλάχιστον 2 κείμενα.")

with tab4:
    tfidf_input = st.text_area("Κείμενο για εξαγωγή λέξεων-κλειδιά:", height=200)
    if st.button("Λέξεις-Κλειδιά"):
        if tfidf_input.strip():
            keywords = extract_keywords(tfidf_input, lang)
            st.markdown("**Top λέξεις:**")
            st.write(keywords)
        else:
            st.warning("Εισήγαγε κάποιο κείμενο.")
