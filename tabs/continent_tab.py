from dash import html, dcc
import dash_bootstrap_components as dbc
from data import cities_df
from data_loader import get_continents
from views.progress_view import render_progress_view

continents = get_continents(cities_df)

def continent_layout():
    return html.Div([
        dbc.Row([

            dbc.Col([
                html.Label("Cap Size"),
                dcc.Slider(
                    id="cap-size-continent",
                    min=100,
                    max=400,
                    step=10,
                    value=200,
                    marks={i: str(i) for i in range(100, 401, 50)},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], width=6),

            dbc.Col([
                html.Label("Continent"),
                dcc.Dropdown(
                    id="dropdown-continent",
                    options=[{"label": c.title(), "value": c} for c in continents],
                    placeholder="Select a continent",
                    className="mb-3"
                )
            ], width=2),

            dbc.Col([
                dbc.Button("Show Continent Stats", id="submit-continent", color="primary", className="mt-4")
            ], width=2, class_name="d-flex justify-content-center"),
            
            dbc.Col([
                dbc.Button("Load Sample Data", id="sample-submit-continent", color="primary", className="mt-4")
            ], width=2, class_name="d-flex justify-content-center")

        ], className="mb-4"),

        render_progress_view('continent')
    ])
