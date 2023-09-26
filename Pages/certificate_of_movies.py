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
st.markdown('This App is Visualization for Certificates of movies on IMDB')

Certificate_Selection = st.selectbox('select Certificate' , ['All Certificates' , 'Select Certificate'])
if Certificate_Selection == 'All Certificates' :
    Certificate = 'All Certificates'
else:
    Certificate = st.multiselect('Select' , df.Certificate.unique()) 

#display
st.header('Movies with Certificates')
display_fig1 = helper.Certificate_of_Movies_with_IMDBrating(Certificate)
st.plotly_chart(display_fig1)

display_fig2 = helper.Certificate_of_Movies_with_Metascore(Certificate)
st.plotly_chart(display_fig2)
