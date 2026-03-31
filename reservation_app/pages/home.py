import streamlit as st
from components.header import branded_header
from components.cards import kpi_card
import datetime

reservations = st.session_state.reservations
restaurants = st.session_state.restaurants

st.markdown(branded_header("🍽️ ReserveIt", "Find and book your perfect table"), unsafe_allow_html=True)

total = len(reservations)
today = datetime.date.today()
upcoming = sum(1 for r in reservations if datetime.date.fromisoformat(r["date"]) >= today)
available = len(restaurants)

col1, col2, col3 = st.columns(3)
col1.markdown(kpi_card("Total Reservations", total, "📊"), unsafe_allow_html=True)
col2.markdown(kpi_card("Upcoming", upcoming, "📅"), unsafe_allow_html=True)
col3.markdown(kpi_card("Restaurants Available", available, "🍽️"), unsafe_allow_html=True)

st.subheader("Welcome to ReserveIt")
st.markdown("ReserveIt helps you discover great restaurants, book tables instantly, and manage your reservations in one place. Easily search by cuisine, date, and party size, and track all your bookings effortlessly.")

st.subheader("Featured Restaurants")

top = sorted(restaurants, key=lambda x: x["rating"], reverse=True)[:4]
cols = st.columns(4)

for col, r in zip(cols, top):
    col.metric(r["name"], f"⭐ {r['rating']}")

if st.button("Search for a Table 🔍"):
    st.switch_page("pages/search.py")