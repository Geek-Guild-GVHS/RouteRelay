import plotly.graph_objects as go
import os

def create_map(lats: list[str]=[], lons: list[str]=[], text: list[str]=[], marker_size=10) -> None:
    """ Args:
        lats (list[str], optional): List of lattitudes to be plotted on the map. Defaults to [].
        lons (list[str], optional): List of longitudes to be plotted on the map. Defaults to [].
        text (list[str], optional): List of text that will be displayed on the map on hover/click. Defaults to [].
        marker_size (int, optional): Size of the marker. Defaults to 10.
    """
    fig = go.Figure(
    go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=marker_size,
        ),
        text=text,
        ),
    )

    fig.layout.mapbox.bounds.north = 22.4
    fig.layout.mapbox.bounds.south = 22.2
    fig.layout.mapbox.bounds.west = 73
    fig.layout.mapbox.bounds.east = 73.4

    fig.layout.mapbox.center.lat = 22.3
    fig.layout.mapbox.center.lon = 73.18
    fig.update_mapboxes(style="open-street-map")
    fig.write_html(f"{os.curdir}/templates/map.html", config={"displayModeBar":False}, full_html=False, default_width="100vw", default_height="80vh")