def extract_skills(text: str, skill_list: list) -> set:
    """
    Extracts skills from text based on a predefined skill list.

    Args:
        text (str): Cleaned resume or JD text
        skill_list (list): List of known skills

    Returns:
        set: Extracted skills found in the text
    """

    text = text.lower()
    found_skills = set()

    for skill in skill_list:
        if skill.lower() in text:
            found_skills.add(skill)

    return found_skills


def find_missing_skills(resume_text: str, jd_text: str, skill_list: list) -> set:
    """
    Finds skills present in JD but missing in resume.

    Returns:
        set: Missing skills
    """

    resume_skills = extract_skills(resume_text, skill_list)
    jd_skills = extract_skills(jd_text, skill_list)

    return jd_skills - resume_skills

if __name__ == "__main__":
    skills = [
        "Python", "Machine Learning", "Data Analysis",
        "SQL", "Git", "Docker"
    ]

    resume = "python machine learning data analysis git"
    jd = "looking for python developer with sql git docker"

    missing = find_missing_skills(resume, jd, skills)

    print("Missing Skills:", missing)
