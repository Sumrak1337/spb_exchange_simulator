from dash import html, dcc
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from ui.layouts.utils import offcanvas, edge_children, make_stylesheet, activity_children


def build_layout() -> html.Div:
    return html.Div([
        dcc.Store(id="network-structure", data={"nodes": [], "edges": []}, storage_type ="session"),
        dcc.Store(id="network-data", data={"supply": [], "demand": [], "transport": []}, storage_type ="session"),
        dcc.Store(id="selected-object", data=None),
        dbc.Button("Добавить узел", id="add-node"),
        dbc.Button("Добавить дугу", id={"type": "open-offcanvas", "name": "add-edge"}),
        html.Div([cyto.Cytoscape(
            id="cyto-network",
            layout={"name": "cose"},
            stylesheet=make_stylesheet(),
            style={
                "width": "70%",
                "height": "700px",
                "backgroundColor": "#ffffff",
            }
        ), html.Div(id="inspector-body", style={"width": "30%"})], style={"display": "flex"}),
        offcanvas(name="add-edge", title="Добавить дугу", children=edge_children()),
        offcanvas(name="add-activity-name", title="Добавить активность", children=activity_children(), width=500),
        html.Div(id="ns-check", style={"marginTop": "300px"}),
    ])
