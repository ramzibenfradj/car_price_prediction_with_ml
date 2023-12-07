import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import seaborn as sns
from main import data 
from dashboard import dashboard_page

# Définir le thème avec un fond noir
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="centered",  # Utilisez "wide" ou "centered"
    initial_sidebar_state="collapsed",  # Utilisez "expanded" ou "collapsed"
) 

if st.button("Dashboard"):
    st.experimental_set_query_params(dashboard=True)

# def dashboard_page():
#     st.header("")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def calculate_correlation_matrix():
    # Replace "your_correlation_matrix.pkl" with the actual path to your pickle file
    with open("your_correlation_matrix.pkl", "rb") as f:
        correlation_matrix = pickle.load(f)
    
    return correlation_matrix

if "dashboard" in st.experimental_get_query_params():
    dashboard_page()
else:

    movies = pickle.load(open("movies_list.pkl", 'rb'))
    similarity = pickle.load(open("similarity.pkl", 'rb'))
    movies_list = movies['title'].values

    # st.header("Movie Recommender System")

    st.markdown(
        """
        <style>
            body {
                border: 5px solid #C61A27;
                padding: 20px;
            }
            .container {
                max-width: 100%;
                margin: auto;
            }
        </style>
        <div class="container">
            <div style="height: 15vh;">
                <h1 style="text-align: center;">Movie Recommendation System🎬</h1>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

    imageUrls = [
        fetch_poster(1632),
        fetch_poster(299536),
        fetch_poster(17455),
        fetch_poster(2830),
        fetch_poster(429422),
        fetch_poster(9722),
        fetch_poster(13972),
        fetch_poster(240),
        fetch_poster(155),
        fetch_poster(598),
        fetch_poster(914),
        fetch_poster(255709),
        fetch_poster(572154)
    ]

    imageCarouselComponent(imageUrls=imageUrls, height=200)

    st.markdown(
        """
        <div style="  ">
            <h1 style="font-size: 3vh; padding:0;  margin-bottom: -35px;">Select movie</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    selectvalue = st.selectbox("", movies_list, key="selector")

    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movie = []
        recommend_poster = []
        for i in distance[1:11]:  # Changed to 11 to include col6 to col10
            movies_id = movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]].title)
            recommend_poster.append(fetch_poster(movies_id))
        return recommend_movie, recommend_poster

    st.markdown(
        """
        <style>
            div[data-baseweb="button"] button[data-key="show_recommend_button"] {
                background-color: #C61A27;
                color: #ffffff;
            }
            # .css-1sy5v53 {
            #     width: 50px;  /* Adjust the width as needed */
            # }

            #titlee{
            padding-bottom:10px;
            text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


    if st.button("Show Recommend" , key="show_recommend_button"):
        movie_name, movie_poster = recommend(selectvalue)
        # col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)  
        col1, col2, col3, col4, col5= st.columns(5)  

        with col1:
            st.image(movie_poster[0])
            st.markdown(f"<div id='titlee'>{movie_name[0]}</div>", unsafe_allow_html=True)
        
        with col2:
            st.image(movie_poster[1])
            st.markdown(f"<div id='titlee'>{movie_name[1]}</div>", unsafe_allow_html=True)
            
        with col3:
            st.image(movie_poster[2])
            st.markdown(f"<div id='titlee'>{movie_name[2]}</div>", unsafe_allow_html=True)
            
        with col4:
            st.image(movie_poster[3])
            st.markdown(f"<div id='titlee'>{movie_name[3]}</div>", unsafe_allow_html=True)    

        col6, col7, col8, col9, col10 = st.columns(5) 
        with col5:
            st.image(movie_poster[4])
            st.markdown(f"<div id='titlee'>{movie_name[4]}</div>", unsafe_allow_html=True)

        with col6:
            st.image(movie_poster[5])
            st.markdown(f"<div id='titlee'>{movie_name[5]}</div>", unsafe_allow_html=True)

        with col7:
            st.image(movie_poster[6])
            st.markdown(f"<div id='titlee'>{movie_name[6]}</div>", unsafe_allow_html=True)

        with col8:
            st.image(movie_poster[7])
            st.markdown(f"<div id='titlee'>{movie_name[7]}</div>", unsafe_allow_html=True)

        with col9:
            st.image(movie_poster[8])
            st.markdown(f"<div id='titlee'>{movie_name[8]}</div>", unsafe_allow_html=True)
            
        with col10:
            st.image(movie_poster[9])
            st.markdown(f"<div id='titlee'>{movie_name[9]}</div>", unsafe_allow_html=True)
            

