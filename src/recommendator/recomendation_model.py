from pandas import Series


class RecommendationModel:

    def __init__(self, movie_id, rate):
        self.movie_id = movie_id
        self.rate = rate

    @staticmethod
    def get_from_ml_recommendations(recommendations: Series) -> list:
        recommendationsToReturn = []
        for movie_id, rate in recommendations.iteritems():
            recommendationsToReturn.append(RecommendationModel(movie_id, rate))

        return recommendationsToReturn

    @staticmethod
    def get_array_ids(recommendations: list) -> list:
        recommendationsIds = []
        for recommendation in recommendations:
            recommendationsIds.append(int(recommendation.movie_id))

        return recommendationsIds
