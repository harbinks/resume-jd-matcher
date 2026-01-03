import re

# -----------------------------
# LOW-SIGNAL (branding / fluff)
# -----------------------------
NOISE_KEYWORDS = [
    "imagine", "phenomenal", "world-class", "customers",
    "proud", "passion", "inspired", "innovation",
    "shopping experience", "leave the world",
    "diversity", "culture", "amazing", "great place",
    "excited", "fast-paced", "dynamic environment"
]

# -----------------------------
# HIGH-SIGNAL (technical + role)
# -----------------------------
SIGNAL_KEYWORDS = [

    # --- Core SDE / Software ---
    "software development", "software engineer", "sde",
    "develop", "design", "build", "implement", "maintain",
    "debug", "troubleshoot", "optimize",
    "architecture", "scalable", "distributed systems",
    "backend", "frontend", "full stack",
    "api", "rest", "microservices",

    # --- Programming Languages ---
    "python", "java", "scala", "c++", "c#", "golang", "go",
    "javascript", "typescript", "node", "nodejs",

    # --- Data / ML / AI ---
    "machine learning", "deep learning", "ml", "ai",
    "llm", "nlp", "data analysis", "model",
    "training", "inference", "feature engineering",

    # --- Automation / QA / Tools ---
    "automation", "automated", "test automation",
    "qa", "quality assurance", "tools development",
    "framework", "workflow",

    # --- DevOps / Infra ---
    "ci/cd", "pipeline", "deployment", "devops",
    "docker", "kubernetes", "cloud",
    "aws", "gcp", "azure",

    # --- Databases / Systems ---
    "sql", "nosql", "database", "data store",
    "performance", "latency", "throughput",

    # --- Engineering Practices ---
    "code review", "design patterns",
    "software lifecycle", "sdlc",
    "testing", "monitoring", "logging"
]



def split_into_sentences(text: str) -> list:
    """Split text into sentences."""
    sentences = re.split(r"[.\n]", text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def is_noise_sentence(sentence: str) -> bool:
    """Check if sentence is mostly branding / fluff."""
    s = sentence.lower()
    return any(word in s for word in NOISE_KEYWORDS)


def is_signal_sentence(sentence: str) -> bool:
    """Check if sentence contains technical / responsibility signal."""
    s = sentence.lower()
    return any(word in s for word in SIGNAL_KEYWORDS)


def clean_job_description(jd_text: str) -> str:
    """
    Remove noise and keep high-signal sentences from JD.

    Returns:
        str: Cleaned, skill-focused JD text
    """
    sentences = split_into_sentences(jd_text)

    filtered = []
    for sent in sentences:
        if is_signal_sentence(sent) and not is_noise_sentence(sent):
            filtered.append(sent)

    return " ".join(filtered)

