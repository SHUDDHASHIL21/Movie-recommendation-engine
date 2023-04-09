import streamlit as st
import pickle
import pandas as pd
import requests
import streamlit.components.v1 as components



#css markdown
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             height : 100%;
             background-image: url("https://images.wallpaperscraft.com/image/single/light_movement_long_exposure_144765_1400x1050.jpg");
             width:100%;
             height:100%; 
             background-attachment: fixed;
             background-size: cover
             background-color: rgba(0, 0, 0, 0)
             
             height:100%;
            
        }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


#css markdown
st.markdown("<h1 <b  style='text-align: center; color: red; font-family: Times New Roman, Times, serif; '> RECOMMENDATION ENGINE </b></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: white; font-family: sans-serif; '>Enter name of a movie or select from the dropdown</p>", unsafe_allow_html=True)


#fetch posters from api
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ddb554075a2561d545e2fee46a3f1851&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#if you give enter a movie name, the function gives you back 5 recommended names
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    posters=[]
    names=[]

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names,posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox(
    "👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇",
    movies['title'].values )

if st.button('Submit'):
    names,posters = recommend(selected_movie)


    col1, col2, col3, col4, col5  = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])



happy = st.slider("How satisfied are you with your experience", min_value=0, max_value=10)
with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your e-mail")
    message = st.text_area("Enter your comment")


    submit = st.form_submit_button("Submit this form")

