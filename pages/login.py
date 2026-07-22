import streamlit as st

from database import SessionLocal

from services.auth_service import authenticate_user


def login_screen():

    st.title("AIMS ERP")

    st.subheader("Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        db = SessionLocal()

        user = authenticate_user(

            db,

            username,

            password

        )

        db.close()

        if user:

            st.session_state.logged_in = True

            st.session_state.user = user.full_name

            st.session_state.role = user.role

            st.rerun()

        else:

            st.error("Invalid Username / Password")
