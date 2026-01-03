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

if __name__ == "__main__":
    sample_texts = [
        "python machine learning data analysis",
        "looking python developer machine learning experience"
    ]

    vectors, vectorizer = vectorize_texts(sample_texts)

    print("TF-IDF shape:", vectors.shape)
    print("Feature names:", vectorizer.get_feature_names_out())

