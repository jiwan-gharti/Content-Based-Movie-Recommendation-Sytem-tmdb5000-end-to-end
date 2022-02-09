import requests

def fetch_api(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9d70f6c25d9edda4a9883622c6dd1873'.format(movie_id))
    data = response.json()
    print(data)
    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500"+ data["poster_path"]