import streamlit as st


def show():

    st.title("Media Roll Production Tracker")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Rolls", 0)

    col2.metric("Inventory", "0 Sq Ft")

    col3.metric("Printed", "0 Sq Ft")

    col4.metric("Remaining", "0 Sq Ft")

    st.divider()

    st.info("Welcome to Version 1")
