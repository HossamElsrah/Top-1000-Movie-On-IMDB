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
st.markdown('This App is Visualization for Movies with High Rating on IMDB')

Rating_Selection = st.selectbox('select Range of Ratings' , ['All Movies' , 'Select Range'])
if Rating_Selection == 'All Movies':
    Rating = 'All Movies'
else:
    Rating = st.multiselect('Select' , df.Range_Rating.unique()) 

#display
st.header('Movies with Range of Ratings')
display_fig = helper.Rating_of_Movies(Rating)
st.plotly_chart(display_fig)
