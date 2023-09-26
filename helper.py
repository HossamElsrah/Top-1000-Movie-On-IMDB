import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import plotly.express as px
from datetime import datetime


@st.cache_data
def load_data():
    df = pd.read_csv('C:/Users/hpc/Desktop/ML/Mid Project/imdb_top_1000_with_movie_type.csv')
    return df

df = load_data()

# Certificate Selection
def Certificate_of_Movies_with_IMDBrating(Certificate):
    if Certificate != 'All Certificates':
        Data = df[df['Certificate'].isin(Certificate)]
    else:
        Data = df
    fig = px.histogram(Data,x='Series_Title', y='IMDB_Rating' ,
                       title='This is Movies with IMDB Rating')
    return fig

def Certificate_of_Movies_with_Metascore(Certificate):
    if Certificate != 'All Certificates':
        Data = df[df.Certificate.isin(Certificate)]
    else:
        Data = df
    fig = px.histogram(Data,x='Series_Title', y='Meta_score' ,
                       title='This is Movies with Meta score')
    return fig




# Rating Selection
def Rating_of_Movies(Rating):
    if Rating != 'All Movies':
        Data = df[df.Range_Rating.isin(Rating)]
    else:
        Data = df
    fig = px.histogram(Data,x='Series_Title', y='IMDB_Rating' ,
                       title='This is Movies with of Ratings')
    return fig




# Type Selection
def Type_of_Movies_with_IMDBrating(Type):
    if Type != 'All Types':
        Data = df[df.Movie_Type.isin(Type)]
    else:
        Data = df
    fig = px.histogram(Data,x='Series_Title', y='IMDB_Rating' ,
                       title='This is Movies with IMDB Rating')
    return fig

def Type_of_Movies_with_metascore(Type):
    if Type != 'All Types':
        Data = df[df.Movie_Type.isin(Type)]
    else:
        Data = df
    fig = px.histogram(Data,x='Series_Title', y='Meta_score' ,
                       title='This is Movies with Meta score')
    return fig




#Director or Star Selection
def Selection_with_IMDBrating(Selection):
    if Selection != 'Directors':
        Data = df[df.Star1.isin(Selection)]
    else :
        Data = df[df.Director.isin(Selection)]
    fig = px.histogram(Data,x='Series_Title', y='IMDB_Rating' ,
                       title='This is Movies with IMDB Rating')
    return fig

def Selection_with_metascore(Selection):
    if Selection == 'Directors':
        Data = df[df.Director.isin(Selection)]
    else :
        Data = df[df.Star1.isin(Selection)]
    fig = px.histogram(Data,x='Series_Title', y='Meta_score' ,
                       title='This is Movies with Meta Score')
    return fig
