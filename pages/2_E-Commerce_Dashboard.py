import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import os

st.title("Dashboard - E-Commerce Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "ECommerce.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "Womens Clothing E-Commerce Reviews.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

type = st.selectbox("Select the Type of Cloth:", df['Class Name'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Class Name'] == type], x="Department Name")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Class Name'] == type], y="Division Name")
col2.plotly_chart(fig_2, use_container_width=True)

st.bar_chart(df['Class Name'])
st.bar_chart(df['Department Name'])
st.bar_chart(df['Division Name'])
st.bar_chart(df['Rating'])

chart_data = pd.DataFrame(df, columns=['Age','Class Name'])
st.line_chart(chart_data)
