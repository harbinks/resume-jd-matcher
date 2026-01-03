import re

# -----------------------------
# Keywords that indicate LOW signal (branding / fluff)
# -----------------------------
NOISE_KEYWORDS = [
    "imagine", "phenomenal", "world-class", "customers",
    "proud", "passion", "inspired", "innovation",
    "shopping experience", "leave the world",
    "diversity", "culture"
]

# -----------------------------
# Keywords that indicate HIGH signal (skills / responsibilities)
# -----------------------------
SIGNAL_KEYWORDS = [
    "develop", "design", "build", "maintain", "implement",
    "automate", "automation", "program", "coding",
    "debug", "deploy", "ci/cd", "pipeline",
    "machine learning", "deep learning", "ml", "ai", "llm",
    "python", "java", "scala", "node", "sql",
    "framework", "system", "architecture"
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

