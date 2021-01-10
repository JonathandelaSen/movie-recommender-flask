import pandas as pd
from pandas import Series
from src.run import app


class ML:

    def __init__(self):
        try:
            self.corr_matrix_movies_ratings = pd.read_csv(
                app.root_path + '/recommendator/ML/data/corr_matrix_movies_ratings_20.csv').corr()
        except FileNotFoundError:
            app.logger.info('Need to create the ML')

    def get_recommendations(self, movies_rating) -> Series:
        app.logger.info('Getting recommendations')
        similar_movies = pd.DataFrame()
        for movie, rate in movies_rating:
            similar_movies = similar_movies.append(self._get_similar(movie, rate), ignore_index=True)
        similar_movies = similar_movies.sum().sort_values(ascending=False).head(20)
        return similar_movies.head(10)

    def _get_similar(self, movie_name, rating):
        similar_ratings = self.corr_matrix_movies_ratings[movie_name] * (rating - 2.5)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings


ml = ML()
