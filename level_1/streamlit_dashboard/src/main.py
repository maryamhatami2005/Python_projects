import streamlit as st
from src.password_generators import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

st.image("/home/mary/project_based_python/projects/level_1/streamlit_dashboard/images/photo_2025-11-25_22-54-03.jpg")
st.title(":closed_lock_with_key: Password Generator")

option = st.radio("Select a password generator",("Pin Code", "Random Password", "Memorable Password"))

if option == "Pin Code":
    length = st.slider("Select the length of the pin code: ",4, 10)
    generator = PinGenerator(length)

elif option == "Random Password":
    length = st.slider("Select the length of the random password: ",8, 14)
    include_symbol = st.toggle("Include symbols:")
    include_number = st.toggle("Include numbers:")
    generator = RandomPasswordGenerator(length, include_number, include_symbol)

elif option == "Memorable Password":
    number_of_words = st.slider("Select the number of words: ", 4, 10)
    seprator = st.text_input("Seperator:", value = "-")
    capitalization = st.toggle("Upper case")
    generator = MemorablePasswordGenerator(number_of_words, seprator, capitalization)

password = generator.generate()
st.write(fr"Your password is: ``` {password} ``` ")
