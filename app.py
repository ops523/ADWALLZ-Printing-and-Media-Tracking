import streamlit as st

from pages.login import login_screen

from pages.dashboard import dashboard

from init_db import initialize_database

initialize_database()

st.set_page_config(

    page_title="AIMS ERP",

    layout="wide"

)

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if not st.session_state.logged_in:

    login_screen()

    st.stop()

##################################################

st.sidebar.title("AIMS ERP")

st.sidebar.write(

    st.session_state.user

)

page = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",

        "Logout"

    ]

)

if page == "Dashboard":

    dashboard()

if page == "Logout":

    st.session_state.logged_in = False

    st.rerun()
