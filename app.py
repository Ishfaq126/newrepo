import pickle
import streamlit as st
import requests

def poster_data(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def load_Recommondations(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    movie_R_Names = []
    movie_R_P = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_R_P.append(poster_data(movie_id))
        movie_R_Names.append(movies.iloc[i[0]].title)

    return movie_R_Names,movie_R_P


st.header('Movie Recommender System')
movies = pickle.load(open('movies_model.pkl','rb'))
similarity = pickle.load(open('recomand_model.pkl','rb'))

list_M = movies['title'].values
selected_movie = st.selectbox(
    "select a movie",
    list_M
)

if st.button('Recommend'):
    movie_R_Names,movie_R_P = load_Recommondations(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(movie_R_Names[0])
        st.image(movie_R_P[0])
    with col2:
        st.text(movie_R_Names[1])
        st.image(movie_R_P[1])

    with col3:
        st.text(movie_R_Names[2])
        st.image(movie_R_P[2])
    with col4:
        st.text(movie_R_Names[3])
        st.image(movie_R_P[3])
    with col5:
        st.text(movie_R_Names[4])
        st.image(movie_R_P[4])





