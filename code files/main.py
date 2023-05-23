import streamlit as st
import home
import Pubs_Location
import Find_Nearest_Pub

PAGES = {
    "Home": home,
    "Pub Locations": Pubs_Location,
    "Find Nearest Pub": Find_Nearest_Pub
}

st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run the app
PAGES[page].run()
