import re
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords (runs only first time)
nltk.download('stopwords')

def clean_text(text: str) -> str:
    """
    Clean input text for NLP processing.
    """

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Remove numbers
    text = re.sub(r'\d+', '', text)

    # 4. Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

