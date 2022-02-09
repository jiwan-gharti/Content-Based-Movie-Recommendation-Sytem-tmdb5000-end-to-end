import streamlit as st
import streamlit.components.v1 as components
from recommend import (
    recommend_movie,
    movies_list
)


# -----------------APP-------------------------------------------
st.header("Tmdb500 Movie Recommender System")
option = st.selectbox(
     'Which movie would you like to watch?',
     movies_list)
recommend_btn =  st.button(label="Recommand")
if recommend_btn:
    recommended_movies, recommended_movies_poster = recommend_movie(option)
    st.write('You selected Movie:')
    st.write(option)
components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)


if recommend_btn:
    col1, col2, col3 = st.columns(3)
    if recommended_movies_poster[0] is not None:
        with col1:
            st.image(recommended_movies_poster[0],caption=recommended_movies[0])
    
    if recommended_movies_poster[1] is not None:
        with col2:
            st.image(recommended_movies_poster[1],caption=recommended_movies[1])
    if recommended_movies_poster[2] is not None:
        with col3:
            st.image(recommended_movies_poster[2],caption=recommended_movies[2])
    if recommended_movies_poster[3] is not None:
        with col1:
            st.image(recommended_movies_poster[3], caption=recommended_movies[3])
    if recommended_movies_poster[4] is not None:
        with col2:
            st.image(recommended_movies_poster[4],caption=recommended_movies[4])

