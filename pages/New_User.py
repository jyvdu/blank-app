import streamlit as st
st.page_link("streamlit_app.py", label="Home")
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div style = "text-align: center;" p class="big-font">Please upload required files for verification.</p>', unsafe_allow_html=True)
st.file_uploader("Scanned copy of Birth Certificate",type=['PDF', 'png','jpg'], accept_multiple_files=True)
st.file_uploader("Scanned copy of Passport",type=['PDF', 'png','jpg'], accept_multiple_files=True)

st.page_link("pages/Success.py", label="Submit")