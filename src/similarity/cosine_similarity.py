from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(tfidf_matrix):
    """
    Calculates cosine similarity between resume and job description.

    Args:
        tfidf_matrix: TF-IDF vectors for resume and JD

    Returns:
        float: similarity score as percentage
    """

    # Cosine similarity between first and second document
    similarity_score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity_score * 100, 2)


