import streamlit as st
from utils import analyze_text

st.set_page_config(page_title="TextLab", layout="wide")
st.title("🔍 Text Feature Extractor & Personalizer")

text_input = st.text_area("Εισήγαγε κείμενο (Ελληνικά ή Αγγλικά):", height=200)

if st.button("Ανάλυση Κειμένου"):
    if text_input.strip():
        with st.spinner("🔎 Αναλύεται..."):
            result = analyze_text(text_input)
            st.subheader("📌 Αποτελέσματα:")
            st.write(result)
    else:
        st.warning("Παρακαλώ εισάγετε κείμενο πρώτα.")
