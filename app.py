import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/ernbilen/Data400_Spring24/main/notes/week11/movies.csv')
df.dropna(inplace=True)

genres = list(df.genre.unique())

with st.sidebar:
    st.write("Here are some instructions.. select widgets bla.")
    year_slider = st.slider(label="Select year:",min_value=1980,max_value=2020,value=(1980,2020))
    genre_selector = st.multiselect("Select genre(s)",genres,default=['Action','Animation','Comedy'])

df = df[(df.year>=year_slider[0])&(df.year<=year_slider[1])]
df = df[df.genre.isin(genre_selector)]


df_grouped = df.groupby('genre')['budget'].sum().reset_index()

st.write('Budget by Genre')
fig = plt.figure(figsize=(20,10))
plt.bar(df_grouped.genre,df_grouped.budget)
plt.xlabel('genre')
plt.ylabel('budget')
st.pyplot(fig)

st.write(df)
