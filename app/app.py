import sys
import os
import streamlit as st

# -------------------------------------------------
# Fix src/ imports when running Streamlit
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# Imports from src pipeline
# -------------------------------------------------
from src.preprocessing.text_cleaner import clean_text
from src.features.tfidf_vectorizer import vectorize_texts
from src.similarity.cosine_similarity import calculate_similarity
from src.skills.skill_extractor import find_missing_skills
from src.utils.pdf_reader import extract_text_from_pdf

# -------------------------------------------------
# Streamlit page config
# -------------------------------------------------
st.set_page_config(
    page_title="Resume–JD Matcher",
    layout="centered"
)

st.title("📄 Resume–Job Description Matcher")
st.write("Check how well your resume matches a job description.")

# -------------------------------------------------
# Resume input section
# -------------------------------------------------
st.subheader("Resume Input")

resume_text_input = st.text_area(
    "Paste Resume Text (optional)",
    height=200,
    placeholder="Paste resume content here..."
)

resume_pdf = st.file_uploader(
    "Or upload Resume PDF",
    type=["pdf"]
)

# -------------------------------------------------
# Job Description input section
# -------------------------------------------------
st.subheader("Job Description Input")

jd_text = st.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Paste job description here..."
)

# -------------------------------------------------
# Skill list (can be expanded later)
# -------------------------------------------------
SKILL_LIST = [
    "Python",
    "Machine Learning",
    "Data Analysis",
    "SQL",
    "Git",
    "Docker",
    "TensorFlow",
    "Deep Learning"
]

# -------------------------------------------------
# Analyze button
# -------------------------------------------------
if st.button("Analyze Match"):

    # -----------------------------
    # Resolve resume input
    # -----------------------------
    resume_text = ""

    if resume_pdf is not None:
        with st.spinner("Extracting text from PDF..."):
            resume_text = extract_text_from_pdf(resume_pdf)
    elif resume_text_input.strip():
        resume_text = resume_text_input
    else:
        st.warning("Please paste resume text or upload a resume PDF.")
        st.stop()

    # -----------------------------
    # Validate JD input
    # -----------------------------
    if not jd_text.strip():
        st.warning("Please paste a job description.")
        st.stop()

    # -----------------------------
    # Run ML pipeline
    # -----------------------------
    with st.spinner("Analyzing resume match..."):
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)

        tfidf_matrix, _ = vectorize_texts(
            [clean_resume, clean_jd]
        )

        match_score = calculate_similarity(tfidf_matrix)

        missing_skills = find_missing_skills(
            clean_resume,
            clean_jd,
            SKILL_LIST
        )

    # -------------------------------------------------
    # Results
    # -------------------------------------------------
    st.subheader("📊 Results")

    st.metric(
        label="Match Score",
        value=f"{match_score}%"
    )

    # Match interpretation
    if match_score >= 70:
        st.success("Strong match ✅")
    elif match_score >= 40:
        st.warning("Moderate match ⚠️")
    else:
        st.error("Low match ❌")

    # Missing skills
    if missing_skills:
        st.write("❌ **Missing Skills:**")
        st.write(", ".join(sorted(missing_skills)))
    else:
        st.success("🎉 No missing skills detected!")
