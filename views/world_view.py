from dash import html
from components.map_temp import map_temp_plot
import dash_bootstrap_components as dbc
import pandas as pd

def render_world_view(df: pd.DataFrame):
    if df is None or df.empty:
        return html.Div("No weather data available.", style={"color": "red"})
    
    return html.Div([
        html.H3(f"Global Weather Dashboard _ {df[['date']].iloc[0,0]}"),
        dbc.Row([
            map_temp_plot(df, width=12)
        ])
    ])