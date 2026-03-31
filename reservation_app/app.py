import streamlit as st

st.set_page_config(page_title="ReserveIt", page_icon="🍽️", layout="wide")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
[data-testid="stHeader"] {display: none;}
footer {visibility: hidden;}
[data-testid="stAppViewBlockContainer"] {padding-top: 1rem;}
.block-container {padding-top: 1rem !important;}
</style>
""", unsafe_allow_html=True)

if "reservations" not in st.session_state:
    st.session_state.reservations = []

if "search_results" not in st.session_state:
    st.session_state.search_results = []

if "search_params" not in st.session_state:
    st.session_state.search_params = {}

if "restaurants" not in st.session_state:
    st.session_state.restaurants = [
        {
            "name": "The Golden Fork",
            "cuisine": "Italian",
            "location": "Downtown",
            "rating": 4.5,
            "price_range": "$$$",
            "available_times": ["6:00 PM", "7:30 PM", "9:00 PM"],
        },
        {
            "name": "Sakura House",
            "cuisine": "Japanese",
            "location": "Midtown",
            "rating": 4.7,
            "price_range": "$$$",
            "available_times": ["5:30 PM", "7:00 PM", "8:30 PM"],
        },
        {
            "name": "Spice Route",
            "cuisine": "Indian",
            "location": "East Side",
            "rating": 4.3,
            "price_range": "$$",
            "available_times": ["6:00 PM", "7:00 PM", "8:00 PM"],
        },
        {
            "name": "Le Petit Bistro",
            "cuisine": "French",
            "location": "West End",
            "rating": 4.6,
            "price_range": "$$$",
            "available_times": ["7:00 PM", "8:30 PM"],
        },
        {
            "name": "Taco Libre",
            "cuisine": "Mexican",
            "location": "Downtown",
            "rating": 4.1,
            "price_range": "$",
            "available_times": ["5:00 PM", "6:30 PM", "8:00 PM", "9:30 PM"],
        },
        {
            "name": "The Wok",
            "cuisine": "Chinese",
            "location": "Chinatown",
            "rating": 4.4,
            "price_range": "$$",
            "available_times": ["5:30 PM", "6:30 PM", "7:30 PM", "8:30 PM"],
        },
        {
            "name": "Olive & Vine",
            "cuisine": "Mediterranean",
            "location": "Midtown",
            "rating": 4.2,
            "price_range": "$$",
            "available_times": ["6:00 PM", "7:30 PM", "9:00 PM"],
        },
        {
            "name": "Burger Barn",
            "cuisine": "American",
            "location": "East Side",
            "rating": 3.9,
            "price_range": "$",
            "available_times": ["5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM"],
        }
    ]

pages = {
    "Browse": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
        st.Page("pages/search.py", title="Search", icon="🔍"),
    ],
    "My Reservations": [
        st.Page("pages/history.py", title="History", icon="📋"),
    ],
}

nav = st.navigation(pages)
nav.run()