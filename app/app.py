import sys
import os
import streamlit as st

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from src.preprocessing.text_cleaner import clean_text
from src.features.tfidf_vectorizer import vectorize_texts
from src.similarity.cosine_similarity import calculate_similarity
from src.skills.skill_extractor import find_missing_skills


st.set_page_config(page_title="Resume–JD Matcher", layout="centered")

st.title("📄 Resume–Job Description Matcher")
st.write("Check how well your resume matches a job description.")

# -----------------------------
# Input areas
# -----------------------------
resume_text = st.text_area(
    "Paste your Resume Text",
    height=200,
    placeholder="Paste resume content here..."
)

jd_text = st.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Paste job description here..."
)

# Skill list (can be expanded later)
skill_list = [
    "Python", "Machine Learning", "Data Analysis",
    "SQL", "Git", "Docker", "TensorFlow", "Deep Learning"
]

# -----------------------------
# Button action
# -----------------------------
if st.button("Analyze Match"):
    if not resume_text or not jd_text:
        st.warning("Please paste both Resume and Job Description.")
    else:
        # Clean text
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)

        # Vectorize
        tfidf_matrix, _ = vectorize_texts([clean_resume, clean_jd])

        # Similarity score
        match_score = calculate_similarity(tfidf_matrix)

        # Missing skills
        missing_skills = find_missing_skills(
            clean_resume, clean_jd, skill_list
        )

        # -----------------------------
        # Output
        # -----------------------------
        st.subheader("📊 Results")

        st.metric(label="Match Score", value=f"{match_score}%")

        if missing_skills:
            st.write("❌ **Missing Skills:**")
            st.write(", ".join(missing_skills))
        else:
            st.success("🎉 No missing skills detected!")
