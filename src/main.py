from src.preprocessing.text_cleaner import clean_text
from src.features.tfidf_vectorizer import vectorize_texts
from src.similarity.cosine_similarity import calculate_similarity
from src.skills.skill_extractor import find_missing_skills


def load_text(file_path: str) -> str:
    """Loads text from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # -----------------------------
    # 1. Load resume & JD
    # -----------------------------
    resume_path = "data/raw/sample_resumes/resume_1.txt"
    jd_path = "data/raw/sample_jds/jd_1.txt"

    resume_text = load_text(resume_path)
    jd_text = load_text(jd_path)

    # -----------------------------
    # 2. Clean text
    # -----------------------------
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    # -----------------------------
    # 3. Vectorize text
    # -----------------------------
    tfidf_matrix, _ = vectorize_texts([clean_resume, clean_jd])

    # -----------------------------
    # 4. Calculate similarity
    # -----------------------------
    match_score = calculate_similarity(tfidf_matrix)

    # -----------------------------
    # 5. Skill extraction
    # -----------------------------
    skill_list = [
        "Python", "Machine Learning", "Data Analysis",
        "SQL", "Git", "Docker", "TensorFlow", "Deep Learning"
    ]

    missing_skills = find_missing_skills(clean_resume, clean_jd, skill_list)

    # -----------------------------
    # 6. Output results
    # -----------------------------
    print("\n====== Resume–JD Match Result ======")
    print(f"Match Score      : {match_score}%")

    if missing_skills:
        print("Missing Skills   :", ", ".join(missing_skills))
    else:
        print("Missing Skills   : None 🎉")

    print("===================================\n")


if __name__ == "__main__":
    main()
