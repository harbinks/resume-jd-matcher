from src.preprocessing.text_cleaner import clean_text
from src.features.tfidf_vectorizer import vectorize_texts
from src.similarity.cosine_similarity import calculate_similarity
from src.skills.skill_extractor import find_missing_skills

from src.jd_processing.jd_cleaner import clean_job_description
from src.scoring.skill_inference import infer_skills_from_text
from src.scoring.skill_coverage import calculate_skill_coverage


def load_text(file_path: str) -> str:
    """Load text from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # -------------------------------------------------
    # 1. Load resume & JD
    # -------------------------------------------------
    resume_path = "data/raw/sample_resumes/resume_1.txt"
    jd_path = "data/raw/sample_jds/jd_1.txt"

    resume_text = load_text(resume_path)
    jd_text = load_text(jd_path)

    # -------------------------------------------------
    # 2. Clean resume & JD
    # -------------------------------------------------
    clean_resume = clean_text(resume_text)

    # De-noise JD (IMPORTANT)
    signal_jd = clean_job_description(jd_text)
    clean_jd = clean_text(signal_jd)

    # -------------------------------------------------
    # 3. Vectorize text (TF-IDF)
    # -------------------------------------------------
    tfidf_matrix, _ = vectorize_texts(
        [clean_resume, clean_jd]
    )

    # -------------------------------------------------
    # 4. Text similarity score
    # -------------------------------------------------
    text_similarity_score = calculate_similarity(tfidf_matrix)

    # -------------------------------------------------
    # 5. Skill inference
    # -------------------------------------------------
    jd_skills = infer_skills_from_text(signal_jd)
    resume_skills = infer_skills_from_text(clean_resume)

    # -------------------------------------------------
    # 6. Skill coverage score
    # -------------------------------------------------
    skill_coverage_score = calculate_skill_coverage(
        jd_skills,
        resume_skills
    )

    # -------------------------------------------------
    # 7. Final weighted score (ATS-style)
    # -------------------------------------------------
    FINAL_SCORE = (
        0.75 * skill_coverage_score +
        0.25 * text_similarity_score
    )
    FINAL_SCORE = round(FINAL_SCORE, 2)

    # -------------------------------------------------
    # 8. Missing skills (JD − Resume)
    # -------------------------------------------------
    missing_skills = jd_skills - resume_skills

    # -------------------------------------------------
    # 9. Output
    # -------------------------------------------------
    print("\n====== Resume–JD Match Result ======")
    print(f"Final Match Score : {FINAL_SCORE}%")
    print(f"Skill Coverage    : {skill_coverage_score}%")
    print(f"Text Similarity   : {text_similarity_score}%")

    if missing_skills:
        print("Missing Skills   :", ", ".join(sorted(missing_skills)))
    else:
        print("Missing Skills   : None 🎉")

    print("===================================\n")


if __name__ == "__main__":
    main()
