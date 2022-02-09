import pickle
from api import fetch_api

movies_dataset = pickle.load(open('movie.pkl','rb'))
movies_list = movies_dataset['title'].values

similarity = pickle.load(open("similarity.pkl",'rb'))

def recommend_movie(movie):
    movie_index = movies_dataset[movies_dataset['title'] == movie.lower()].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse= True, key=lambda x: x[1])[1:6]

    recommended_movies_name = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = i[0]
        #fetch poster form API
        recommended_movies_poster.append(fetch_api(movie_id=movie_id))
        recommended_movies_name.append(movies_dataset.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster