import json

from ..recommendator.ML.ml import ml
from ..movies.movies_service import get_movies_by_ids
from .recomendation_model import RecommendationModel
from flask import jsonify


def get_recommendations():
    recommendations = ml.get_recommendations([("1", 5), ("3", 3), ("12", 1), ("6", 2)])
    recommendationObjects = RecommendationModel.get_from_ml_recommendations(recommendations)
    movies = get_movies_by_ids(RecommendationModel.get_array_ids(recommendationObjects))
    return json.dumps([movie.dump() for movie in movies])
