# api.py

import hug
from falcon import HTTP_404

MOVIES = [
    {
        'id': '1c35ce50-1eed-11e6-b6ba-3e1d05defe78',
        'title': 'The Matrix',
        'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his roles in the war against its controllers',
    }
]

@hug.get()
def movies():
    return {
        'objects' : MOVIES
    }

@hug.get('/movies/{movie_id}/')
def movie(movie_id, response):
  movie_ids = map(lambda x: x['id'], MOVIES)

  if movie_id not in movie_ids:
    response.status = HTTP_404
    return 'Not found'

  movie = MOVIES[movie_ids.index(movie_id)]
