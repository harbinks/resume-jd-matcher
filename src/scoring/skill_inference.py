# Canonical skill map with aliases
SKILL_MAP = {
    "Python": ["python"],
    "Java": ["java"],
    "C++": ["c++", "cpp"],
    "JavaScript": ["javascript", "js"],
    "SQL": ["sql"],
    "NoSQL": ["nosql", "mongodb", "dynamodb"],
    "Machine Learning": ["machine learning", "ml"],
    "Deep Learning": ["deep learning", "dl"],
    "LLM": ["llm", "large language model"],
    "Data Structures": ["data structures", "dsa"],
    "Algorithms": ["algorithms"],
    "Distributed Systems": ["distributed system", "distributed systems"],
    "REST APIs": ["rest api", "restful"],
    "CI/CD": ["ci/cd", "pipeline", "pipelines"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes", "k8s"],
    "AWS": ["aws", "amazon web services"],
    "DevOps": ["devops"],
    "Automation": ["automation", "automated"],
    "Testing": ["testing", "test automation"],
    "React": ["react", "reactjs"],
    "Angular": ["angular", "angularjs"]
}


def infer_skills_from_text(text: str) -> set:
    """
    Infer canonical skills from raw text using alias matching.
    """
    text = text.lower()
    found_skills = set()

    for skill, aliases in SKILL_MAP.items():
        for alias in aliases:
            if alias in text:
                found_skills.add(skill)
                break

    return found_skills

