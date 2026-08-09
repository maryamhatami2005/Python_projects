import streamlit as st
from deepface import DeepFace

import os
from utils import display_prediction

def predict_sex_and_race_from_image(img_path):

    try:
        faces= DeepFace.analyze(img_path = "img4.jpg", actions = ['gender', 'race'])
        if faces:
            return faces[0].get("Dominant_gender", "Unknow"), faces[0].get("Dominant_race", "Unknown")
        else:
            return "No face detected", "No face detected"

    except:
        return f"Error: {str(e)}", f"Error: {str(e)}"


def process_image_input():
    uploaded_file = st.file_uploader(f"Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        with st.spinner('Predicting...'):
            # Save the uploaded file temporarily
            with open("temp_image.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())

            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Uploaded Image", width=200)

            with col2:
                sex, race = predict_sex_and_race_from_image("temp_image.jpg")
                display_prediction(sex, race)

            # Remove the temporary file
            os.remove("temp_image.jpg")
