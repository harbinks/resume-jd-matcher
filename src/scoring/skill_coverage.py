def calculate_skill_coverage(jd_skills: set, resume_skills: set) -> float:
    """
    Calculate how many JD-required skills are covered by the resume.

    Returns:
        float: coverage percentage (0–100)
    """

    if not jd_skills:
        return 0.0

    matched_skills = jd_skills.intersection(resume_skills)
    coverage = len(matched_skills) / len(jd_skills)

    return round(coverage * 100, 2)



    score = calculate_skill_coverage(jd_skills, resume_skills)
    print("Skill Coverage Score:", score, "%")
