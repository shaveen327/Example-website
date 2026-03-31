import streamlit as st
from components.header import branded_header
import datetime

if "restaurants" not in st.session_state:
    st.session_state.restaurants = []

if "search_results" not in st.session_state:
    st.session_state.search_results = []

if "search_params" not in st.session_state:
    st.session_state.search_params = {}

if "reservations" not in st.session_state:
    st.session_state.reservations = []

restaurants = st.session_state.restaurants
cuisine = sorted(set(r["cuisine"] for r in restaurants))

st.markdown(
    branded_header("🔍 Find a Table", "Search by cuisine, date, and party size"),
    unsafe_allow_html=True
)

with st.form("reservation_form"):
    selectedCuisine = st.selectbox("Cuisine", ["All"] + cuisine)
    partySize = st.slider("Party Size", 1, 20, 2)
    date = st.date_input("Date", datetime.date.today())
    preferredTime = st.selectbox(
        "Preferred Time",
        ["Any","5:00 PM","5:30 PM","6:00 PM","6:30 PM","7:00 PM","7:30 PM","8:00 PM","8:30 PM","9:00 PM","9:30 PM"]
    )
    specialRequests = st.text_area(
        "Special Requests",
        placeholder="Allergies, celebrations, seating preferences...",
        height=100
    )
    submitted = st.form_submit_button("Search Restaurants")

if submitted:
    filteredresults = restaurants.copy()

    if selectedCuisine != "All":
        filteredresults = [r for r in filteredresults if r["cuisine"] == selectedCuisine]

    if preferredTime != "Any":
        filteredresults = [r for r in filteredresults if preferredTime in r["available_times"]]

    st.session_state.search_results = filteredresults
    st.session_state.search_params = {
        "date": str(date),
        "party_size": partySize,
        "special_requests": specialRequests
    }

results = st.session_state.search_results
params = st.session_state.search_params

if results and params:
    st.success(f"Found {len(results)} restaurants matching your criteria")

    for rest in results:
        with st.expander(f"🍽️ {rest['name']}"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"**Cuisine:** {rest['cuisine']}")
                st.markdown(f"**Location:** {rest['location']}")
                st.markdown(f"**Price Range:** {rest['price_range']}")
                st.markdown(f"**Rating:** ⭐ {rest['rating']}")

            with col2:
                selected_time = st.selectbox(
                    "Select a Time",
                    rest["available_times"],
                    key=f"time_{rest['name']}"
                )

            if st.button("Book This Table", key=f"book_{rest['name']}"):
                reservation = {
                    "restaurant": rest["name"],
                    "cuisine": rest["cuisine"],
                    "date": params["date"],
                    "time": selected_time,
                    "party_size": params["party_size"],
                    "special_requests": params["special_requests"],
                    "status": "Confirmed"
                }

                st.session_state.reservations.append(reservation)
                st.toast(f"Reservation confirmed at {rest['name']}!")
                st.balloons()

elif submitted:
    st.warning("No restaurants match your filters. Try broadening your search.")