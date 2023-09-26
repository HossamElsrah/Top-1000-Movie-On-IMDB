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
st.markdown('This App is Visualization for Directors with Ratings on IMDB')

Selection = st.selectbox('Select' , ['Directors' , 'Stars'])
if Selection == 'Directors':
    Selection = st.multiselect('Select Director' , df.Director.unique())
else :
    Selection = st.multiselect('Select Star' , df.Star1.unique())

#display
st.header('Movies with Select of Director or Movie Star')
display_fig1 = helper.Selection_with_IMDBrating(Selection)
st.plotly_chart(display_fig1)

display_fig2 = helper.Selection_with_metascore(Selection)
st.plotly_chart(display_fig2)