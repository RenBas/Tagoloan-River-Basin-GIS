import folium
from streamlit_folium import st_folium


def create_map(geojson_data):
    """
    Create the interactive Leaflet map.
    """

    m = folium.Map(
        location=[8.43, 124.74],
        zoom_start=10,
        control_scale=True
    )

    folium.GeoJson(
        geojson_data,
        name="Tagoloan River Basin"
    ).add_to(m)

    folium.LayerControl().add_to(m)

    st_folium(
        m,
        width=None,
        height=700
    )
