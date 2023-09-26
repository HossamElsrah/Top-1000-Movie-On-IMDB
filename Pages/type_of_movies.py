import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import plotly.express as px
from datetime import datetime
import helper

df = helper.load_data()


st.title('Top 1000 movis on IMDB')
st.markdown('This App is Visualization for Types of movies on IMDB')

Type_Selection = st.selectbox('select Type' , ['All Types' , 'Select Type'])
if Type_Selection == 'All Types' :
    Type = 'All Types'
else:
    Type = st.multiselect('Select' , df.Movie_Type.unique()) 

#display
st.header('Movies with Types')
display_fig1 = helper.Type_of_Movies_with_IMDBrating(Type)
st.plotly_chart(display_fig1)

display_fig2 = helper.Type_of_Movies_with_metascore(Type)
st.plotly_chart(display_fig2)
