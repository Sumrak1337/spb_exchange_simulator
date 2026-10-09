from dash import Dash, Input, Output, State, MATCH, html, ALL
import dash_bootstrap_components as dbc

from ui.layouts.utils import inspector_parameters, build_node_inspector, \
    build_edge_inspector


def button_callback(app: Dash):
    @app.callback(
        Output({"type": "offcanvas", "name": MATCH}, "is_open"),
        Input({"type": "open-offcanvas", "name": MATCH}, "n_clicks"), prevent_initial_call=True,)
    def open_offcanvas(_n):
        return True

    @app.callback(Output("network-structure", "data", allow_duplicate=True),
                  Input("add-node", "n_clicks"),
                  [State("network-structure", "data")], prevent_initial_call=True)
    def add_node(_n, ns):
        for idx in range(1000):
            node_name = f"node{idx}"
            if node_name not in ns["nodes"]:
                ns["nodes"].append(node_name)
                return ns

    @app.callback(
        Output("network-structure", "data"),
        Input("save-edge", "n_clicks"),
        [State("network-structure", "data"),
         State({"type": "dropdown-node", "name": ALL}, "value")
         ], prevent_initial_call=True
    )
    def save_edge_button(_n, ns, edge):
        if edge not in ns["edges"] and None not in edge:
            ns["edges"].append(edge)
        return ns

    @app.callback(Output("ns-check", "children"),
                  Input("network-structure", "data"))
    def storage_check(ns):
        return html.Div([f"nodes: {ns['nodes']}, edges: {ns['edges']}"])

    @app.callback(Output("cyto-network", "elements"),
                  Input("network-structure", "data"))
    def update_cyto_network(ns):
        elements = []
        for node in ns["nodes"]:
            elements.append({"data": {"id": node, "label": node, "object_type": "node"}})

        for node1, node2 in ns["edges"]:
            elements.append({"data": {"id": f"{node1}|{node2}", "source": node1, "target": node2, "object_type": "edge"}})

        return elements

    @app.callback(Output({"type": "dropdown-node", "name": MATCH}, "options"),
                  Input("network-structure", "data"))
    def update_dropdown(ns):
        return ns["nodes"]

    @app.callback(Output("selected-object", "data", allow_duplicate=True),
                  Input("cyto-network", "tapNodeData"), prevent_initial_call=True)
    def set_selected_node(data):
        return data

    @app.callback(Output("selected-object", "data", allow_duplicate=True),
                  Input("cyto-network", "tapEdgeData"), prevent_initial_call=True)
    def set_selected_edge(data):
        return data

    @app.callback(Output("network-structure", "data", allow_duplicate=True),
                  Output("inspector-body", "children", allow_duplicate=True),
                  Input({"type": "delete-node", "node": MATCH}, "n_clicks"),
                  [State("network-structure", "data"),
                   State({"type": "delete-node", "node": MATCH}, "id"),
                   State("inspector-body", "children"),
                   ], prevent_initial_call=True)
    def delete_node(n_clicks, ns, btn_id, inspector):
        if n_clicks:
            current_node = btn_id["node"]
            ns["nodes"] = [node for node in ns["nodes"] if node != current_node]
            ns["edges"] = [edge for edge in ns["edges"] if current_node not in edge]
            inspector = html.Div()
        return ns, inspector

    @app.callback(Output("network-structure", "data", allow_duplicate=True),
                  Output("inspector-body", "children", allow_duplicate=True),
                  Input({"type": "delete-edge", "source": MATCH, "target": MATCH}, "n_clicks"),
                  [State("network-structure", "data"),
                   State({"type": "delete-edge", "source": MATCH, "target": MATCH}, "id"),
                   State("inspector-body", "children"),
                   ], prevent_initial_call=True)
    def delete_edge(n_clicks, ns, btn_id, inspector):
        if n_clicks:
            source = btn_id["source"]
            target = btn_id["target"]
            ns["edges"] = [edge for edge in ns["edges"] if edge != [source, target]]
            inspector = html.Div()
        return ns, inspector


    @app.callback([Output("inspector-body", "children", allow_duplicate=True),
                  Output("cyto-network", "tapNodeData")],
                  Input("cyto-network", "tapNodeData"),
                  [State("network-data", "data")],
                  prevent_initial_call=True)
    def update_node_inspector(node_data, network_data):
        if node_data:
            return build_node_inspector(node=node_data["id"], network_data=network_data), None
        return html.Div(), None

    @app.callback([Output("inspector-body", "children", allow_duplicate=True),
                  Output("cyto-network", "tapEdgeData")],
                  Input("cyto-network", "tapEdgeData"),
                  [State("network-data", "data")],
                  prevent_initial_call=True)
    def update_edge_inspector(edge_data, network_data):
        if edge_data:
            return build_edge_inspector(edge_data=edge_data, network_data=network_data), None
        return html.Div(), None

