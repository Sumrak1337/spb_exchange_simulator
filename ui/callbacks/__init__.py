from dash import Dash

from ui.callbacks.button_calbacks import button_callback


def register_callbacks(app: Dash):
    button_callback(app=app)
