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
    if not name:
        st.warning("Please enter your name.")
    else:
        st.write(f"Welcome to the world, {name}!")


client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input=f"write a 100 word about how old the person is, depending on your view on their {age}, you don't have to be polite, just be funny and sarcastic.",
)
st.subheader("Your age description")
st.write(response.output_text)