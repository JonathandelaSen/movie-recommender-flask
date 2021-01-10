FROM python:3.9-slim

ADD requirements /MoviesRecommender1API/src/requirements


RUN pip install -r /MoviesRecommender1API/src/requirements/pro.txt --no-cache-dir

ADD . /app/MoviesRecommender1API
WORKDIR /app/MoviesRecommender1API

CMD  gunicorn -c gunicorn/config.py wsgi:app