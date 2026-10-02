from dash import Dash, Input, Output, State, ctx, html, dcc
import dash_bootstrap_components as dbc

def button_callback(app: Dash):
    @app.callback(Output("cyto-network", "elements"),
              Input("btn-add-save", "n_clicks"),
              State("cyto-network", "elements"))
    def update_elements(btn_add_save, elements):
        return elements

    @app.callback(Output("offcanvas", "title"),
                  Output("offcanvas", "is_open"),
                  Output("offcanvas", "children"),
                  Input("btn-add-node", "n_clicks"),
                  Input("btn-add-edge", "n_clicks"),
                  [State("offcanvas", "is_open")])
    def toggle_offcanvas(n_node, n_edge, is_open):
        if ctx.triggered_id == "btn-add-node":
            is_open_ = not is_open if n_node else is_open
            content = html.Div([
                dcc.Input(placeholder="Название узла"),
                dcc.Input(placeholder="Название материала"),
                dcc.Input(placeholder="Название периода"),
                html.Hr(),
                dbc.Button("Создать узел", id="save-btn")
            ])
            return "Добавить узел", is_open_, content
        elif ctx.triggered_id == "btn-add-edge":
            is_open_ = not is_open if n_edge else is_open
            content = html.Div()
            return "edge", is_open_, content
        return "kavo", False, html.Div()

