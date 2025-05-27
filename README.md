## TextLabApp – Εφαρμογή NLP για Ανάλυση Κειμένου, Clustering & Λέξεις-Κλειδιά
Το TextLabApp είναι μια διαδραστική εφαρμογή Streamlit για επεξεργασία φυσικής γλώσσας (NLP), που παρέχει ανάλυση συναισθήματος, σύγκριση κειμένων, clustering, εξαγωγή λέξεων-κλειδιών, καθώς και δυνατότητα εισαγωγής CSV αρχείων ή εξαγωγής αναρτήσεων από Reddit μέσω API.

🔗 Live Demo
👉 Δες την εφαρμογή σε δράση!

## Δυνατότητες
📄 Ανάλυση Συναισθήματος Κειμένου (multilingual BERT)
🆚 Σύγκριση Δύο Κειμένων με cosine similarity
🔗 Clustering Πολλαπλών Κειμένων μέσω sentence embeddings + KMeans
🧠 Εξαγωγή Λέξεων-Κλειδιών με TF-IDF
📂 Ανάλυση CSV Αρχείου: Επέλεξε στήλη και ανάλυσε μαζικά τα κείμενα
🗨️ Reddit API Integration: Απόκτησε αναρτήσεις από συγκεκριμένα subreddits & keywords για επεξεργασία

## Εγκατάσταση
git clone https://github.com/yourusername/textlabapp.git
cd textlabapp
pip install -r requirements.txt
streamlit run app.py

## Δομή Έργο
textlabapp/
│
├── app.py               # Κύριο αρχείο Streamlit UI
├── utils.py             # Βοηθητικές NLP συναρτήσεις
├── requirements.txt     # Python εξαρτήσεις
└── README.md            # Τρέχον αρχείο οδηγιών

## Εξαρτήσεις
streamlit
trnsformers
sentence-transformers
scikit-learn
pandas, numpy
praw (Reddit API)

## Για εγκατάσταση όλων:
pip install -r requirements.txt

## Χρήση
Απλώς τρέξε το:
streamlit run app.py

## Tabs:
📄 Ανάλυση Κειμένου: Συναισθηματική ανάλυση και παρουσίαση με emoji.
🆚 Σύγκριση: Cosine similarity μεταξύ δύο κειμένων.
🔗 Clustering: Ομαδοποίηση παρόμοιων κειμένων.
🧠 Λέξεις-Κλειδιά: Εξαγωγή σημαντικότερων όρων.
📂 CSV Ανάλυση: Ανέβασε αρχείο CSV και ανάλυσε στήλες κειμένου.
📡 Reddit Extractor: Εισήγαγε subreddit και λέξη-κλειδί για εξαγωγή και ανάλυση περιεχομένου.

## Ρυθμίσεις API (προαιρετικά για Reddit)
Δημιούργησε ένα .env αρχείο ή πρόσθεσε μεταβλητές περιβάλλοντος:
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_agent_name

## Μελλοντικές Επεκτάσεις
Export σε Excel / PDF
Σύνδεση με Twitter API / Meta Graph
Εμφάνιση αποτελεσμάτων με διαγράμματα
Προφίλ χρήστη με login

## Συνεισφορά
Είσαι ευπρόσδεκτος/η να συνεισφέρεις με ιδέες, pull requests ή bugs! Δημιούργησε ένα issue ή κάνε fork.

## Άδεια
Ανοιχτού κώδικα υπό την άδεια MIT.
