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
        font-size: 16px;
	}
}
</style>""",
unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/New_User.py", label = "PDF not in Database")

with col2:
    st.page_link("pages/Returning_Flyer.py", label = "PDF in Database")


