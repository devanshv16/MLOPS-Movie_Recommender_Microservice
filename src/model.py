import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load dataset
movies = pd.read_csv("data/movies.csv")  # Columns: movieId, title, genres
movies["genres"] = movies["genres"].fillna("")


# Convert genres into a TF-IDF matrix
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

# print("Training Nearest Neighbors model...")

# Use Nearest Neighbors instead of full cosine similarity
nn_model = NearestNeighbors(
    n_neighbors=6, metric="cosine", algorithm="auto"
)  # 6 because first is itself
nn_model.fit(tfidf_matrix)

# print("Nearest Neighbors model trained successfully!")


def recommend_movies(movie_title, num_recommendations=5):
    # Check if movie exists
    if movie_title not in movies["title"].values:
        return ["Movie not found in dataset."]

    # Get index of the movie
    idx = movies[movies["title"] == movie_title].index[0]

    # Find nearest neighbors
    _, indices = nn_model.kneighbors(
        tfidf_matrix[idx], n_neighbors=num_recommendations + 1
    )

    # Get recommended movie titles (excluding input movie)
    recommended_movies = movies.iloc[indices[0][1:]]["title"].tolist()

    return recommended_movies


# Example usage
if __name__ == "__main__":
    movie_name = input("Enter the name of your preferred movie: ")
    recommendations = recommend_movies(movie_name, 5)
    print("\nRecommended Movies:")
    for movie in recommendations:
        print(movie)
