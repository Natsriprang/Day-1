import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

st.header("Welcome")
name = st.text_input("What is your name?")
age = 28
You_are_a_great_lawyer = True
st.write(f"{len(name)}/100")
age = st.text_input("How old are you?")
st.write(f"{len(age)}/100")
if st.button("Submit"):
    st.write(f"Welcome to the world! {name}")


client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input="write a 100 word about how old the person is, depending on your view, you don't have to be polite.",
)
st.write(response.output_text)