from dash import html
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc


def build_layout() -> html.Div:
    return html.Div([
        dbc.Button("Добавить узел", id="btn-add-node", n_clicks=0),
        dbc.Button("Добавить дугу", id="btn-add-edge", n_clicks=0),
        cyto.Cytoscape(
            id="cyto-network",
            layout={"name": "cose"},
            elements=[]
        ),
        dbc.Offcanvas(
            id="offcanvas",
            title="TitleNode",
            is_open=False,
            placement="start",
            backdrop=True,
            style={'width': 300},
        ),
    ])
