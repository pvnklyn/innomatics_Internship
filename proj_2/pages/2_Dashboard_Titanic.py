import streamlit as st
from matplotlib import image
import os

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

st.title("Dashboard - Titanic Data")

img = image.imread(image_path1)
st.image(img)

df = pd.read_csv(data_path1)
st.dataframe(df)

sex = st.selectbox("Select the species:",df["Sex"].unique())

#col1, col2 = st.columns(2)

st.subheader('Histogram')
fig_1 = px.histogram(df[df['Sex'] == sex], x="Survived")
st.plotly_chart(fig_1, use_container_width=True)

st.subheader('Box plot')
fig_2 = px.box(df[df['Sex'] == sex], y="Survived")
st.plotly_chart(fig_2, use_container_width=True)