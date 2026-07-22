import streamlit as st
import sqlite3
import bcrypt

DB = "database/media_rolls.db"


def login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.title("Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        conn = sqlite3.connect(DB)

        cur = conn.cursor()

        cur.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        row = cur.fetchone()

        conn.close()

        if row:

            if bcrypt.checkpw(
                password.encode(),
                row[0].encode()
            ):
                st.session_state.logged_in = True
                st.rerun()

        st.error("Invalid username/password")

    return False
