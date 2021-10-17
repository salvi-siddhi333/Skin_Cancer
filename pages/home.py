import streamlit as st


def app():
    #title to home page
    st.header("Welcome to")
    st.title("Skin Cancer Prediction Model")
    #Image path
    st.image("./images/bg.jpg")
    #Simple text to project
    st.write("This model that allows and helps user to predict the image having cancer cell present or not!")