from pathlib import Path
import json
import streamlit as st


def load_geojson():
    """
    Load the Tagoloan River Basin GeoJSON file.

    Returns
    -------
    dict
        Parsed GeoJSON object.
    """

    data_path = Path("data") / "tagoloan.geojson"

    if not data_path.exists():
        st.error(f"GeoJSON file not found: {data_path}")
        st.stop()

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        st.error(f"Unable to read GeoJSON.\n\n{e}")
        st.stop()
