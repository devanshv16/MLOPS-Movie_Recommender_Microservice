from src.model import recommend_movies
import fire


def cli(movie_title: str = "Interstellar (2014)", num_recommendations: int = 5):
    """
        Command-line interface for the movie recommendation system.
    p

        Args:
            movie_title (str): The title of the movie.
            num_recommendations (int, optional): Number of recommendations. Defaults to 5.

        Returns:
            List of recommended movies.
    """
    recommendations = recommend_movies(movie_title, num_recommendations)

    print("\nRecommended Movies:")
    for movie in recommendations:
        print("-", movie)


if __name__ == "__main__":
    fire.Fire(cli)
