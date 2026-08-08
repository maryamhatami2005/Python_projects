import streamlit as st
from name_predictor import name_input

if __name__ == "__main__":
    st.title(f"Gender and Race Prediction")

    input_type= st.radio("Choose input type:" ,  ("Name", "Image"))

    if input_type == "Name":
        name_input

    else:
        pass