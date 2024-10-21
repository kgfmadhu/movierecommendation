import streamlit as st
import pandas as pd
import pickle
import base64
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda s: s[1])[1:6]
    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



movies_list=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open("similarity.pkl","rb"))
st.title('Movie Recommendation System')
selected_movie=st.selectbox("select a movie",movies["title"].values)
if st.button("Recommend"):
    recommendation_movies=recommend(selected_movie)
    for i in recommendation_movies:
        st.write(i)

