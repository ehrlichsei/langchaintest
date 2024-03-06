import langchain_helper as lch
import streamlit as st


st.title("Pets name generator")

user_animal_type = st.sidebar.selectbox("what is your pet?", ("Cat", "Dog", "Cow"))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label = "What color is your Cat?", max_chars=15)

elif user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label = "What color is your Dog?", max_chars=15)

elif user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label = "What color is your Cow?", max_chars=15)


if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])