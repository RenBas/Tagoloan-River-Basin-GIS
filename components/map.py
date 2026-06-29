import folium
from streamlit_folium import st_folium

from utils.styles import (
    style_function,
    highlight_function
)


def create_map(geojson):

    m = folium.Map(
        location=[8.42, 124.74],
        zoom_start=10,
        control_scale=True,
        tiles="OpenStreetMap"
    )

    folium.GeoJson(
        geojson,

        name="Tagoloan River Basin",

        style_function=style_function,

        highlight_function=highlight_function,

        tooltip=folium.GeoJsonTooltip(

            fields=[
                "name",
                "type"
            ],

            aliases=[
                "Name",
                "Feature Type"
            ],

            sticky=False
        ),

        popup=folium.GeoJsonPopup(
            fields=list(
                geojson["features"][0]["properties"].keys()
            )
        )

    ).add_to(m)

    folium.LayerControl().add_to(m)

    st_folium(
        m,
        width=None,
        height=700
    )
