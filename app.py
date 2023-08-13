import streamlit as st
import pickle
import requests
import urllib.request
import webbrowser


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f6137ddd27f478bf4fe96b8287e25878&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    mov_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_pages = []

    for i in mov_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_pages.append(dataset.iloc[i[0]].homepage)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_pages


st.title('Cineaste Recommender')

dataset = pickle.load(open('plcset.pkl', 'rb'))
movies = pickle.load(open('movies.pkl', 'rb'))
movie_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

mov_name = st.selectbox(
    'Which movies do you like?',
    movie_list
)

if st.button('Recommend'):
    recoms, recom_posters, recom_pages = recommend(mov_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recom_posters[0])
        st.write(f'''
            <a target="_self" href={recom_pages[0]}>
                <button>
                    {recoms[0]}
                </button>
            </a>
            ''',
                 unsafe_allow_html=True
                 )

    with col2:
        st.image(recom_posters[1])
        st.write(f'''
                    <a target="_self" href={recom_pages[1]}>
                        <button>
                            {recoms[1]}
                        </button>
                    </a>
                    ''',
                 unsafe_allow_html=True
                 )

    with col3:
        st.image(recom_posters[2])
        st.write(f'''
                            <a target="_self" href={recom_pages[2]}>
                                <button>
                                    {recoms[3]}
                                </button>
                            </a>
                            ''',
                unsafe_allow_html=True
                )

    with col4:
        st.image(recom_posters[3])
        st.write(f'''
                            <a target="_self" href={recom_pages[3]}>
                                <button>
                                    {recoms[3]}
                                </button>
                            </a>
                            ''',
                unsafe_allow_html=True
                )

    with col5:
        st.image(recom_posters[4])
        st.write(f'''
                            <a target="_self" href={recom_pages[3]}>
                                <button>
                                    {recoms[4]}
                                </button>
                            </a>
                            ''',
                unsafe_allow_html=True
                )

    st.write('You selected:', mov_name)
else:
    st.write('Goodbye')





