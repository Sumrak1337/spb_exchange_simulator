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
