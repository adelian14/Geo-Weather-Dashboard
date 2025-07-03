from dash import html, dcc
import dash_bootstrap_components as dbc
from data import cities_df
from data_loader import get_countries
from views.progress_view import render_progress_view

countries = get_countries(cities_df)

def region_layout():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.Label("Cap Size"),
                dcc.Slider(
                    id="cap-size-region",
                    min=10,
                    max=100,
                    step=2,
                    value=20,
                    marks={i: str(i) for i in range(10, 101, 10)},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], width=4),
            
            dbc.Col([
                html.Label("Country"),
                dcc.Dropdown(
                    id="country-dropdown-region",
                    options=[{"label": c.title(), "value": c} for c in countries],
                    placeholder="Choose a country",
                    className="mb-3"
                )
            ], width=2),
            
            dbc.Col([
                html.Label("region"),
                dcc.Dropdown(
                    id="dropdown-region",
                    placeholder="Choose a region",
                    className="mb-3"
                )
            ], width=2),

            dbc.Col([
                dbc.Button("Show region Sample", id="submit-region", color="primary", className="mt-4")
            ], width=2, class_name="d-flex justify-content-center"),
            
            dbc.Col([
                dbc.Button("Load Sample Data", id="sample-submit-region", color="primary", className="mt-4")
            ], width=2, class_name="d-flex justify-content-center")

        ], className="mb-4"),

        render_progress_view("region")
    ])
