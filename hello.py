import pandas as pd
import streamlit as st
import pickle
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    receommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        # fetch poster
        receommended_movies.append(movies.iloc[i[0]].title)
    return receommended_movies

movie_dict=pickle.load(open('movie_dict_new.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity_new.pkl','rb'))

st.title("Movie Recommender System ")

selected_movie_name =st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)