import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Hr.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "HRDataset_v14.csv")

st.title("Dashboard - Human Resources Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

dept = st.selectbox("Select the Department:", df['Department'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Department'] == dept], x="EmpID")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Department'] == dept], y="Position")
col2.plotly_chart(fig_2, use_container_width=True)

st.bar_chart(df['Department'])
st.bar_chart(df['Position'])

chart_data = pd.DataFrame(df, columns=['Department','Position'])
st.line_chart(chart_data)
