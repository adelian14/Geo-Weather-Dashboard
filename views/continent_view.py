from dash import dash_table, html

def render_continent_view(df):
    if df is None or df.empty:
        return html.Div("No weather data available.", style={"color": "red"})
    
    return dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": col, "id": col} for col in df.columns],
        style_table={'overflowX': 'auto', 'maxHeight': '500px', 'overflowY': 'auto'},
        style_cell={
            'minWidth': '100px', 'width': '150px', 'maxWidth': '250px',
            'whiteSpace': 'normal',
            'textAlign': 'left',
        },
        style_header={
            'backgroundColor': '#f2f2f2',
            'fontWeight': 'bold'
        },
        page_size=12,
        fixed_rows={'headers': True}
    )