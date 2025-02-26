import streamlit as st
from streamlit.components.v1 import html
st.set_page_config(page_title='Home Page', page_icon="🫆", layout='wide')
st.markdown("""
<style>
	[data-testid="stDecoration"] {
		background-image: linear-gradient(90deg, rgb(187, 187, 187), rgb(187, 187, 187));
        decoration.innerText = "BioImmigration";
        display: block;
        text-align: left;
        font-size: 20px;
	}
    button {
    height: 50px;
    width: 200px;
    color: blue;
}
</style>""",
unsafe_allow_html=True)

st.markdown("""
<style>

    button {
    height: 50px;
    width: 200px;
    color: blue;
}
</style>""",
unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.link_button("PDF is not in the database", "pages/New_User.py")

with col2:
    st.link_button("PDF in Database","pages/Returning_Flyer.py")
#st.link_button("Go to gallery", "https://streamlit.io/gallery")

