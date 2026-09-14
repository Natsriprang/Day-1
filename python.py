import streamlit as st
st.header("Welcome")
name = st.text_input("What is your name?")
age = 28
You_are_a_great_lawyer = True
st.write(f"{len(name)}/100")
age = st.text_input("How old are you?")
st.write(f"{len(age)}/100")
if st.button("Submit"):
    st.write(f"Welcome to the world! {name}")

user = {"name": "name", "age": int(user["age"])}
if user["age"] < 24:
#if statement is false, it will not show the message below
    st.write("You were born this millenium")
else:
    st.write("You were born last millenium")


