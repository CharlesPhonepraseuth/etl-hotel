# Third party imports
from dash import html

# Local application imports
from views.partials import navbar


### Create Layout ###
def serve_layout():

    layout = html.Div([
        navbar.create_navbar(),

        html.Br(),

        html.H1('Visual analysis app'),

        html.Br(),

    ], style = {'alignItems': 'center', 'min-height': '101vh'})

    return layout
