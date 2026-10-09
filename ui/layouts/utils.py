import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

def offcanvas(*, name: str, title: str, children: dbc.Container, width=300):
    return dbc.Offcanvas(
        children,
        id={"type": "offcanvas", "name": name},
        title=title,
        placement="start",
        scrollable=True,
        backdrop=True,
        style={'width': width},
    )

def edge_children() -> dbc.Container:
    return dbc.Container([
        dcc.Dropdown(id={"type": "dropdown-node", "name": "from"}, placeholder="Выберите пункт отправления"),
        dcc.Dropdown(id={"type": "dropdown-node", "name": "to"}, placeholder="Выберите пункт назначения"),
        html.Hr(),
        dbc.Button("Сохранить", id="save-edge")
    ], id={"type": "container", "name": "edge"})

def activity_children() -> dbc.Container:
    return dbc.Container([
        dcc.Dropdown(id="activity-node-type", options=["supply", "demand"], placeholder="Вид активности"),
        dbc.Input(id="activity-product", placeholder="Название материала"),
        dbc.Button("Сохранить", id="save-activity", style={"marginTop": "20ppx"})
    ])

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

def build_node_inspector(node, network_data):
    return html.Div([
        html.H3("Активность узла"),
        html.Hr(),

        # add cards

        html.Div([
            dbc.Button(id={"type": "rename-node", "node": node}, children="Переименовать", style={"backgroundColor": "#4568d9", "opacity": 0.75, "width": "33%"}),
            dbc.Button(id="add-activity", children="Добавить активность", style={"backgroundColor": "#e6b217", "opacity": 0.75, "width": "33%"}),
            dbc.Button(id={"type": "delete-node", "node": node}, children="Удалить узел", style={"backgroundColor": "#b52626", "opacity": 0.75, "width": "33%"}),
        ]
        ),
        html.Div(id="edit-field")
    ]
    )

def build_edge_inspector(edge_data, network_data):
    return html.Div([
        html.H3("Активность дуги"),
        html.Hr(),

        # add cards

        html.Div([
            dbc.Button(id={"type": "add-activity", "context": "edge", "id": edge_data["id"]}, children="Добавить активность", style={"backgroundColor": "#e6b217", "opacity": 0.75, "width": "50%"}),
            dbc.Button(id={"type": "delete-edge", "source": edge_data["source"], "target": edge_data["target"]}, children="Удалить дугу", style={"backgroundColor": "#b52626", "opacity": 0.75, "width": "50%"}),
        ]
        )
    ]
    )
