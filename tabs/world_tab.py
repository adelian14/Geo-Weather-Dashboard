from dash import html, dcc
import dash_bootstrap_components as dbc
from views.progress_view import render_progress_view

def world_layout():
    return dbc.Row([

        dbc.Col([
            html.Label("Cap Size"),
            dcc.Slider(
                id="cap-size-world",
                min=100,
                max=400,
                step=10,
                value=200,
                marks={i: str(i) for i in range(100, 401, 50)},
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ], width=8),

        dbc.Col([
            dbc.Button("Generate World Data", id="submit-world", color="primary", className="mt-4")
        ], width=2, class_name="d-flex justify-content-center"),
        
        dbc.Col([
            dbc.Button("Load Sample Data", id="sample-submit-world", color="primary", className="mt-4")
        ], width=2, class_name="d-flex justify-content-center"),
        
        render_progress_view('world')
        
    ], className="mb-4")

