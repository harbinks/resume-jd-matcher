from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize_texts(texts: list):
    """
    Converts a list of cleaned texts into TF-IDF vectors.

    Args:
        texts (list): List of cleaned text strings

    Returns:
        tfidf_matrix: TF-IDF numerical representation
        vectorizer: Fitted TF-IDF vectorizer
    """

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(texts)

    return tfidf_matrix, vectorizer



