from dash import html, dcc
import dash_bootstrap_components as dbc
from data import cities_df
from data_loader import get_countries
from views.progress_view import render_progress_view

countries = get_countries(cities_df)

def city_layout():
    return html.Div([
        dbc.Row([

            dbc.Col([
                html.Label("Country"),
                dcc.Dropdown(
                    id="country-dropdown-city",
                    options=[{"label": c.title(), "value": c} for c in countries],
                    placeholder="Choose a country",
                    className="mb-3"
                )
            ], width=4),

            # Region Dropdown
            dbc.Col([
                html.Label("Region"),
                dcc.Dropdown(
                    id="region-dropdown-city",
                    placeholder="Choose a region",
                    className="mb-3"
                )
            ], width=4),

            # City Dropdown
            dbc.Col([
                html.Label("City"),
                dcc.Dropdown(
                    id="dropdown-city",
                    placeholder="Choose a city",
                    className="mb-3"
                )
            ], width=2),

            # Submit Button
            dbc.Col([
                dbc.Button("Show City Data", id="submit-city", color="primary", className="mt-4")
            ], width=2)

        ], className="mb-4"),

        render_progress_view("city")
    ])
