import requests

from src.movies.movie_model import Movie

from src.settings import Settings


def get_movies_external_api(platform_movies_ids) -> list:
    movies = []

    for platform_movies_id in platform_movies_ids:
        movies.append(get_movie_external_api(platform_movies_id['tmdbId']))

    return movies


def get_movie_external_api(tmdb_id) -> Movie:
    res = requests.get(_get_api_url(tmdb_id))
    movie = Movie.from_tmdb_json(res.json())
    return movie


def _get_api_url(tmdb_id) -> str:
    return "https://api.themoviedb.org/3/movie/%s?api_key=%s" % (tmdb_id, Settings.TMDB_APY_KEY)
