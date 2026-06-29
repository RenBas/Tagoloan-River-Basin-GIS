"""
Centralized cartographic styling for the Tagoloan River Basin Web GIS.
"""

def style_function(feature):
    feature_type = feature["properties"].get("type", "")

    styles = {
        "hec_hms_domain": {
            "color": "#145A32",
            "weight": 4,
            "fillColor": "#145A32",
            "fillOpacity": 0.05,
        },

        "sub_basin": {
            "color": "#2E86C1",
            "weight": 2,
            "fillColor": "#85C1E9",
            "fillOpacity": 0.35,
        },

        "river": {
            "color": "#2166F3",
            "weight": 3,
            "opacity": 1.0,
        }
    }

    return styles.get(
        feature_type,
        {
            "color": "#808080",
            "weight": 1,
            "fillOpacity": 0.2,
        }
    )


def highlight_function(feature):
    return {
        "weight": 5,
        "color": "#F39C12",
        "fillOpacity": 0.60,
    }
