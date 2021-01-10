from src.run import mongo


class Movie:

    def __init__(self):
        self.title = None
        self.overview = None
        self.vote_average = None
        self.poster_path = None
        self.genres = []

    @staticmethod
    def get_platform_ids(ids) -> list:
        return list(
            mongo.db.movies_ids.find({"movieId": {"$in": ids}}, {"_id": 0, "movieId": 1, "imdbId": 1, "tmdbId": 1}))

    @staticmethod
    def from_tmdb_json(tmdb_movie):
        movie = Movie()
        movie.title = tmdb_movie['title']
        movie.overview = tmdb_movie['overview']
        movie.vote_average = tmdb_movie['vote_average']
        movie.poster_path = "https://image.tmdb.org/t/p/w500/%s" % tmdb_movie['poster_path']
        movie.genres = Movie._get_genres_from_json(tmdb_movie['genres'])
        return movie

    def dump(self):
        return {
            'movie': self.title,
            'overview': self.overview,
            'vote_average': self.vote_average,
            'poster_path': self.poster_path,
            'genres': self.genres,
        }

    @staticmethod
    def _get_genres_from_json(genres):
        genres_list = []
        for genre in genres:
            genres_list.append(genre['name'])

        return genres_list
