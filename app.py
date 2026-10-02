from dash import Dash

from ui.layouts.main_layout import build_layout
from ui.callbacks import register_callbacks
import dash_bootstrap_components as dbc

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.FLATLY])

app.layout = build_layout()
register_callbacks(app=app)


if __name__ == "__main__":
    app.run(debug=True)
