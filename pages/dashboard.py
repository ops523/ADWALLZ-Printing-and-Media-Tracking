import streamlit as st


def dashboard():

    st.title("Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Open Rolls",
        "0"
    )

    c2.metric(
        "Today's Production",
        "0 Sq Ft"
    )

    c3.metric(
        "Packages",
        "0"
    )

    c4.metric(
        "Dispatch Pending",
        "0"
    )

    st.divider()

    st.write(
        "Welcome to AIMS ERP"
    )
