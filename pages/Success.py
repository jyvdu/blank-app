import streamlit as st
st.page_link("streamlit_app.py", label="Back to Home")
st.markdown("""
<style>
.big-font {
    font-size:70px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div style = "text-align: center;" p class="big-font">Thank you for submitting the requirements.</p>', unsafe_allow_html=True)

st.logo(image="https://en.wikipedia.org/wiki/Cup_of_Joe_(band)#/media/File:Logo_of_Cup_of_Joe_(band).png",size="large", link="https://upload.wikimedia.org/wikipedia/en/d/d8/Logo_of_Cup_of_Joe_%28band%29.png")