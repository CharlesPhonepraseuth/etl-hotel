# Third party imports
from dash.dependencies import Input, Output

# Local application imports
from app import app
from views import home, hotel_analysis


def register_router():

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):

        if pathname == '/':
            return home.serve_layout()
        elif pathname == '/hotel-analysis':
            return hotel_analysis.serve_layout()
        else:
            # TODO : PAGE 404
            return True
