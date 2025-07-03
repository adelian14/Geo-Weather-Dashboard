from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px

def map_temp_plot(df, width=12):
    
    df = df.copy()
    lat_min = df['lat'].min() - 0.2
    lat_max = df['lat'].max() + 0.2
    lon_min = df['lon'].min() - 0.2
    lon_max = df['lon'].max() + 0.2
    df["temp_size"] = df["temp_c"] - df["temp_c"].min() + 1
    df["condition"] = df["condition_text"]
    
    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lon",
        color="temp_c",
        size="temp_size",
        hover_name="country",
        hover_data={
            "region": True,
            "temp_c": True,
            "temp_size": False,
            "condition": True,
            "city": False,
            "lat": False,
            "lon": False
        },
        color_continuous_scale="RdYlBu_r",
        projection="natural earth",
        title="World Temperature Map"
    )
    fig.update_geos(
        lataxis_range=[lat_min, lat_max],
        lonaxis_range=[lon_min, lon_max],
        visible=False,
        resolution=50,
        showcountries=True
    )
    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor="rgb(229, 229, 229)",
            showcountries=True,
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        height=600
    )

    return dbc.Col([
        dcc.Graph(figure=fig)
    ], width=width)
