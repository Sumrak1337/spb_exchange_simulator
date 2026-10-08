from dash import Dash, Input, Output, State, MATCH, html, ALL
import dash_bootstrap_components as dbc

def button_callback(app: Dash):
    @app.callback(
        Output({"type": "offcanvas", "name": MATCH}, "is_open"),
        Input({"type": "open-offcanvas", "name": MATCH}, "n_clicks"), prevent_initial_call=True,)
    def open_offcanvas(_n):
        return True

    @app.callback(
        Output("network-structure", "data"),
        Input({"type": "save", "name": MATCH}, "n_clicks"),
        [State("network-structure", "data"),
         State("node-name", "value"),
         State({"type": "dropdown-node", "name": ALL}, "value")
         ], prevent_initial_call=True
    )
    def save_button(_n, ns, name, value):
        if name not in ns["nodes"] and name is not None:
            ns["nodes"].append(name)

        if value not in ns["edges"] and None not in value:
            ns["edges"].append(value)

        return ns

    @app.callback(Output("ns-check", "children"),
                  Input("network-structure", "data")
                  )
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

    @app.callback(Output("selected-object", "data"),
                  Input("cyto-network", "tapEdgeData"))
    def set_selected_edge(data):
        return data

    @app.callback(Output("network-structure", "data", allow_duplicate=True),
                  Output("selected-object", "data", allow_duplicate=True),
                  Input("delete-object", "n_clicks"),
                  [State("network-structure", "data"),
                   State("selected-object", "data")], prevent_initial_call=True)
    def delete_object(_n, ns, selected):
        if selected["object_type"] == "node":
            ns["nodes"] = [node for node in ns["nodes"] if node != selected["id"]]
            ns["edges"] = [edge for edge in ns["edges"] if selected["id"] not in edge]
        elif selected["object_type"] == "edge":
            ns["edges"] = [edge for edge in ns["edges"] if edge != [selected["source"], selected["target"]]]
        return ns, None
