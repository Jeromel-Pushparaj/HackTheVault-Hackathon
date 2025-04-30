# === STEP 1: Import and Load Dataset ===
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from utils import asker

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load CSV
df = pd.read_csv(r'D:\HackTheVault-Hackathon\utils\UpdatedResumeDataSet.csv')
df = df.drop_duplicates()

# === STEP 2: Preprocessing ===
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = nltk.word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    words = [stemmer.stem(w) for w in words]
    return ' '.join(words)

df['Resume_Processed'] = df['Resume'].apply(preprocess_text)

# === STEP 3: Vectorization ===
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = tfidf.fit_transform(df['Resume_Processed'])
y = df['Category']

# === STEP 4: Train Classifier ===
model = RandomForestClassifier()
model.fit(X, y)

# === STEP 5: Predict Category of New Resume ===
# "skilled in Python, machine learning, data analysis, and Pandas" 
# new_resume = str(input("Enter skill: "))
def predictDomain(new_resume):
    processed_resume = preprocess_text(new_resume)
    resume_vector = tfidf.transform([processed_resume])
    predicted_category = model.predict(resume_vector)
    print("Predicted Category:", predicted_category[0])
    return predicted_category[0]

# === STEP 6: Suggest Top Skills for a Given Role ===
def suggest_skills_for_role(role_input, top_n=20):
    matching_resumes = df[df['Category'].str.lower() == role_input.lower()]
    
    if matching_resumes.empty:
        print(f"No resumes found for role: {role_input}")
        return

    transformed_resumes = tfidf.transform(matching_resumes['Resume_Processed'])
    summed_tfidf = transformed_resumes.sum(axis=0)
    feature_names = tfidf.get_feature_names_out()
    
    word_scores = [(feature_names[i], summed_tfidf[0, i]) for i in range(len(feature_names))]
    top_skills = sorted(word_scores, key=lambda x: x[1], reverse=True)[:top_n]

    print(f"\nTop {top_n} skills for '{role_input}':")
    for rank, (skill, score) in enumerate(top_skills, start=1):
        print(f"{rank}. {skill}")

    output = f"\nTop {top_n} skills for '{role_input}':\n"
    output += "\n".join([f"{rank}. {skill}" for rank, (skill, score) in enumerate(top_skills, start=1)])
    prompt = "Recomand a courses or resources for this skills in a structured way " + output
    return asker.skillRecommand(prompt)

# === STEP 7: Ask User for Role and Show Suggested Skills ===
# role = input("Enter a job role to get suggested skills: ")
# suggest_skills_for_role(role)
