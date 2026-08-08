import countryflag
import streamlit as st
from names_dataset import NameDataset, NameWrapper

from utils import display_prediction


def load_names_dataset():
    return NameDataset()

nd =  load_names_dataset()

def predict_sex_and_race_from_name(name):
    result = NameWrapper(nd.search(name)).describe.strip(',')

    if len(result) > 0:
        sex = result[0]
    else:
        sex= "Unknown"

    if len(result) > 0:
        country = result[1]
    else:
        country = "Unknown"

    if country != "Unknown":
        flag = countryflag.getflag([country])
        country = f"{flag} {country}"

    return sex, country


def name_input():
    name = st.text_input(f"Enter a name: ")
    if name:
        with st.spinner('Predicting...'):
            sex, country = predict_sex_and_race_from_name(name)
            display_prediction(sex, country)
