import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px

st.title("Dashboard - Youtube Data")

img = image.imread("resources/images/ytimg.jpeg")
st.image(img)

df = pd.read_csv("resources/data/Top YouTube Channels Data .csv")
st.dataframe(df)

st.subheader("Subscribers Distribution")
category = st.selectbox("Select the Category:", df['category '].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['category '] == category], x="subscribers ")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['category '] == category], y="subscribers ")
col2.plotly_chart(fig_2, use_container_width=True)

st.subheader("Top 10 Channels")
st.write(df.head(10))
fig_3 = px.bar(df.head(10), x="youtuber", y="subscribers ")
st.plotly_chart(fig_3, use_container_width=True)
