import streamlit as st
base = 'light'
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">BioImmigration Air</p>', unsafe_allow_html=True)


st.page_link("streamlit_app.py", label="Home")
st.page_link("pages/New_User.py", label="No PDF in database")
st.page_link("pages/Returning_Flyer.py", label="PDF in database")


