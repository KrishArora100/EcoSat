import streamlit as st
import plotly.express as px
import pandas as pd
import os
from os import listdir


df = pd.read_csv("1007227/1007227_2020.csv")

dates = df["Timestamp"].to_list()


facility = "1007227"
facility = st.text_input(label="Facility Id", value = "1007227")

year = "2020"
year = st.selectbox(label="Year", options=('2020', '2011', '2012', '2013', '2014', '2015', \
                                    '2016', '2017', '2018', '2019', '2021'),
                    placeholder="2020")

timestamp = dates[0]
timestamp = st.selectbox(label="Timestamp", options=dates,
                    placeholder=dates[0])

if facility != "1007227":
    st.caption("This facility is a work in progress. Please enter \"1007227\"")

if year != "2020":
    st.caption("This year is a work in progress. Please enter \"2020\"")

 
rgb_dir = "1007227/rgb_color_imgs/" + timestamp + ".jpg"
smoke_seg_dir = "1007227/smoke_seg_imgs/" + timestamp + ".jpg"
smoke_contours_dir = "1007227/smoke_contours_imgs/" + timestamp + ".jpg"


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Actual Image")
   st.image(rgb_dir, width=200)

with col2:
   st.header("Smoke Plumes")
   st.image(smoke_seg_dir, width=213)

with col3:
   st.header("Contours")
   st.image(smoke_contours_dir, width=213)



