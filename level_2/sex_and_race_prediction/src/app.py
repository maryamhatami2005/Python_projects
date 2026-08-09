import streamlit as st
from name_predictor import process_name_input
from image_predictor import process_image_input


if __name__ == "__main__":
    st.title("Gender and Race Prediction")

    input_type = st.radio("Choose input type:", ("Name", "Image"))

    if input_type == "Name":
        process_name_input()
    else:
        process_image_input()