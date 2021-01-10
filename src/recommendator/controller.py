from src.run import app
from ..recommendator.recommendation_service import get_recommendations


@app.route('/recommendation')
def recommendation():
    return get_recommendations()
