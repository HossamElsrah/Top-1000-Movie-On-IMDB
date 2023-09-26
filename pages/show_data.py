import streamlit as st
import pandas as pd



@st.cache_data
def load_data():
    df = pd.read_csv('imdb_top_1000_with_movie_type.csv')
    return df

df = load_data()

st.title('Top 1000 movis on IMDB')
st.markdown('This App is for show The Data from Top 1000 Movie on IMDB Rating')

if st.checkbox('Show Data'):
    st.write(df)
