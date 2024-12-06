import streamlit as st
st.title("Welcome to PracRes Air!")

st.header("Please select an option.")
st.page_link("streamlit_app.py", label="Home")
st.page_link("pages/page_1.py", label="No PDF in database")
st.page_link("pages/page_2.py", label="PDF in database")
