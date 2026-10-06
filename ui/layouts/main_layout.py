from dash import html, dcc
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from ui.layouts.utils import offcanvas, node_children, edge_children


def build_layout() -> html.Div:
    return html.Div([
        dcc.Store(id="network-structure", data={"nodes": [], "edges": []}, storage_type ="session"),
        dcc.Store(id="network-data", data={"supply": [], "demand": [], "transport": []}, storage_type ="session"),
        dbc.Button("Добавить узел", id={"type": "open-offcanvas", "name": "add-node"}),
        dbc.Button("Добавить дугу", id={"type": "open-offcanvas", "name": "add-edge"}),
        cyto.Cytoscape(
            id="cyto-network",
            layout={"name": "cose"},
            elements=[],
            style={
                "width": "100%",
                "height": "550px",
                "backgroundColor": "#ffffff",
            }
        ),
        offcanvas(name="add-node", title="Добавить узел", children=node_children()),
        offcanvas(name="add-edge", title="Добавить дугу", children=edge_children()),
        html.Div(id="ns-check"),
    ])
