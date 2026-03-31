import streamlit as st
from components.header import branded_header
import pandas as pd

st.markdown(branded_header("📋 My Reservations", "View and manage your bookings"), unsafe_allow_html=True)

if not st.session_state.reservations:
    st.info("You haven't made any reservations yet.")
    if st.button("Browse Restaurants"):
        st.switch_page("pages/search.py")
    st.stop()

reservations = st.session_state.reservations

st.dataframe(reservations, use_container_width=True)

st.subheader("Cancel a Reservation")

options = [
    f"{r['restaurant']} — {r['date']} at {r['time']}"
    for r in reservations
]

selected = st.selectbox("Select a reservation to cancel", options)

if st.button("Cancel Selected Reservation"):
    index = options.index(selected)
    st.session_state.reservations.pop(index)
    st.toast("Reservation cancelled.")
    st.rerun()