# Third party imports
import dash
import dash_bootstrap_components as dbc


### Dash instance ###
app = dash.Dash(__name__, suppress_callback_exceptions = True, external_stylesheets = [dbc.themes.SPACELAB, './assets/styles.css'])
