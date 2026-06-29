import streamlit as st

from utils.loader import load_geojson
from components.map import create_map


st.set_page_config(
    page_title="Tagoloan River Basin GIS",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Tagoloan River Basin GIS")

st.write(
    "Stage 1 — Interactive GIS Foundation"
)

geojson = load_geojson()

create_map(geojson)
