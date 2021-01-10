from .movie_model import Movie
from .movie_provider import get_movies_external_api


def get_movies_by_ids(ids):
    return get_movies_external_api(Movie.get_platform_ids(ids))

