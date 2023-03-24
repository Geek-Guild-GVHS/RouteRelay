import plotly.graph_objects as go
import os

def create_map(lats: list[str]=[], lons: list[str]=[], text: list[str]=[], marker_size=10) -> None:
    """Create a plotly map.

    No parameters are compulsory.

    Args:
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
        )
    )

    fig.update_mapboxes(style="open-street-map")
    fig.write_html(f"{os.getcwd()}/templates/map.html", config={"displayModeBar":False})