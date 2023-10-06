# Standard library imports
import os

# Third party imports
from dash import dcc, html

# Local application imports
from app import app
from router import register_router
from callbacks import hotel_callback


### Set app layout ###
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

### Set up router ###
register_router()

### Set up callbacks ###
hotel_callback.register_callbacks(app)


if __name__ == '__main__':
    port = os.environ.get('DASH_HTTP_PORT')

    app.run_server(debug = True, host = '0.0.0.0', port = port)
