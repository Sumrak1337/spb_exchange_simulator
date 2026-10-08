import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

def offcanvas(*, name: str, title: str, children: dbc.Container):
    return dbc.Offcanvas(
        children,
        id={"type": "offcanvas", "name": name},
        title=title,
        placement="start",
        scrollable=True,
        backdrop=True,
        style={'width': 300},
    )

def node_children() -> dbc.Container:
    return dbc.Container([
        dbc.Input(id="node-name", placeholder="Название узла"),
        html.Hr(),
        dbc.Button("Сохранить", id={"type": "save", "name": "node"})
    ], id={"type": "container", "name": "node"},)

def edge_children() -> dbc.Container:
    return dbc.Container([
        dcc.Dropdown(id={"type": "dropdown-node", "name": "from"}, placeholder="Выберите пункт отправления"),
        dcc.Dropdown(id={"type": "dropdown-node", "name": "to"}, placeholder="Выберите пункт назначения"),
        html.Hr(),
        dbc.Button("Сохранить", id={"type": "save", "name": "edge"})
    ], id={"type": "container", "name": "edge"})

def parameters_panel() -> dbc.Container:
    return dbc.Container(
        html.Div([
            html.H2("Параметры"),
            html.Div([
                dbc.Button("+ Добавить активность", style={"backgroundColor": "#e6b217", "opacity": 0.75, "width": "50%"}),
                dbc.Button(id="delete-object", children="Удалить", style={"backgroundColor": "#b52626", "opacity": 0.75, "width": "50%"})
            ], style={"display": "flex"}
            )
        ]))

def make_stylesheet():
    stylesheet = [
        {
            "selector": "node",
            "style": {
                "content": "data(label)",
                "width": 70,
                "height": 70,
                "text-wrap": "wrap",
                "font-size": "10px",
                "text-valign": "center",
                "text-halign": "center",
                "color": "#0c2a45",
                "font-weight": "bold",
                "label-font": "sans-serif",
            },
        },
        {
            "selector": "edge",
            "style": {
                "target-arrow-shape": "triangle",
                "arrow-scale": 0.75,
                "curve-style": "bezier",
            }
        }
    ]
    return stylesheet
