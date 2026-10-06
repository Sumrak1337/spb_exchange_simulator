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
         State("node-name", "value")], prevent_initial_call=True
    )
    def save_button(_n, ns, name):
        if name not in ns["nodes"] and name is not None:
            ns["nodes"].append(name)
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
            elements.append({"data": {"id": node, "label": node}})
        return elements

    @app.callback(Output({"type": "dropdown-node", "name": MATCH}, "options"),
                  Input("network-structure", "data"))
    def update_dropdown(ns):
        return ns["nodes"]
