import sys
import os
import streamlit as st

# -------------------------------------------------
# Fix src imports
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# Pipeline imports
# -------------------------------------------------
from src.preprocessing.text_cleaner import clean_text
from src.features.tfidf_vectorizer import vectorize_texts
from src.similarity.cosine_similarity import calculate_similarity

from src.jd_processing.jd_cleaner import clean_job_description
from src.scoring.skill_inference import infer_skills_from_text
from src.scoring.skill_coverage import calculate_skill_coverage
from src.utils.pdf_reader import extract_text_from_pdf

# -------------------------------------------------
# Streamlit config
# -------------------------------------------------
st.set_page_config(page_title="Resume–JD Matcher", layout="centered")
st.title("📄 Resume–Job Description Matcher")
st.write("ATS-style resume matching using skills + similarity")

# -------------------------------------------------
# Resume input
# -------------------------------------------------
st.subheader("Resume Input")

resume_text_input = st.text_area(
    "Paste Resume Text (optional)",
    height=200
)

resume_pdf = st.file_uploader(
    "Or upload Resume PDF",
    type=["pdf"]
)

# -------------------------------------------------
# JD input
# -------------------------------------------------
st.subheader("Job Description Input")

jd_text = st.text_area(
    "Paste Job Description",
    height=200
)

# -------------------------------------------------
# Analyze button
# -------------------------------------------------
if st.button("Analyze Match"):

    # -----------------------------
    # Resolve resume input
    # -----------------------------
    if resume_pdf:
        resume_text = extract_text_from_pdf(resume_pdf)
    elif resume_text_input.strip():
        resume_text = resume_text_input
    else:
        st.warning("Please provide resume text or upload a PDF.")
        st.stop()

    if not jd_text.strip():
        st.warning("Please provide a job description.")
        st.stop()

    # -----------------------------
    # Run pipeline
    # -----------------------------
    with st.spinner("Analyzing resume..."):

        # Clean resume
        clean_resume = clean_text(resume_text)

        # Clean + de-noise JD
        signal_jd = clean_job_description(jd_text)
        clean_jd = clean_text(signal_jd)

        # TF-IDF similarity
        tfidf_matrix, _ = vectorize_texts(
            [clean_resume, clean_jd]
        )
        text_similarity_score = calculate_similarity(tfidf_matrix)

        # Skill inference
        jd_skills = infer_skills_from_text(signal_jd)
        resume_skills = infer_skills_from_text(clean_resume)

        # Skill coverage
        skill_coverage_score = calculate_skill_coverage(
            jd_skills,
            resume_skills
        )

        # Final weighted score
        FINAL_SCORE = round(
            0.75 * skill_coverage_score +
            0.25 * text_similarity_score,
            2
        )

        missing_skills = jd_skills - resume_skills

    # -------------------------------------------------
    # Results
    # -------------------------------------------------
    st.subheader("📊 Results")

    st.metric("Final Match Score", f"{FINAL_SCORE}%")

    col1, col2 = st.columns(2)
    col1.metric("Skill Coverage", f"{skill_coverage_score}%")
    col2.metric("Text Similarity", f"{text_similarity_score}%")

    if FINAL_SCORE >= 70:
        st.success("Strong match ✅")
    elif FINAL_SCORE >= 40:
        st.warning("Moderate match ⚠️")
    else:
        st.error("Low match ❌")

    if missing_skills:
        st.write("❌ **Missing Skills:**")
        st.write(", ".join(sorted(missing_skills)))
    else:
        st.success("🎉 No missing skills detected!")
