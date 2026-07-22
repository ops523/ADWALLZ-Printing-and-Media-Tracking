import streamlit as st

from database import init_database

from auth import login

from modules import dashboard
from modules import inventory
from modules import production
from modules import wastage
from modules import reports
from modules import settings

st.set_page_config(
    page_title="Media Roll Tracker",
    layout="wide"
)

init_database()

if not login():
    st.stop()

st.sidebar.title("ADWALLZ")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Inventory",
        "Production",
        "Wastage",
        "Reports",
        "Settings"
    ]
)

if page == "Dashboard":
    dashboard.show()

elif page == "Inventory":
    inventory.show()

elif page == "Production":
    production.show()

elif page == "Wastage":
    wastage.show()

elif page == "Reports":
    reports.show()

elif page == "Settings":
    settings.show()
