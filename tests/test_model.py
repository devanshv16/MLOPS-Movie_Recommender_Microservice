# from src import model
from src import recommend_movies


def test_valid_movie():
    movie_name = "Interstellar (2014)"  # Ensure this exists in movies.csv
    recommendations = recommend_movies(movie_name, 5)
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0  # It should return some recommendations


def test_invalid_movie():
    movie_name = "Some Random Movie"
    recommendations = recommend_movies(movie_name, 5)
    assert recommendations == ["Movie not found in dataset."]


def test_empty_movie():
    recommendations = recommend_movies("", 5)
    assert recommendations == ["Movie not found in dataset."]


def test_num_recommendations():
    movie_name = "Interstellar (2014)"
    recommendations = recommend_movies(movie_name, 3)
    assert len(recommendations) == 3  # Should return exactly 3 recommendations
