import streamlit as st


st.title("My Simple Streamlit App")
st.write("Hello, Streamlit!")


name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")