# Third party imports
from dash import dcc, html, dash_table

# Local application imports
from views.partials import navbar


### Create Layout ###
def serve_layout():

    rank_options = [
        {'label': '1', 'value': 1},
        {'label': '3', 'value': 3},
        {'label': '5', 'value': 5},
        {'label': '10', 'value': 10}
    ]

    layout = html.Div([
        navbar.create_navbar(),

        html.Main([

            html.Br(),

            html.H1("French Hotel Dashboard"),

            html.Br(),

            html.Div([

                html.Div([
                    html.Div(['Hotel count'], className='card-header'),
                    html.Div([
                        html.P(id='hotel-count-output', className='card-text nb')
                    ], className='card-body')
                ],className='card border-primary mb-3'),

                html.Div([
                    html.Div([
                        'Rating average'
                    ], className='card-header'),
                    html.Div([
                        html.P(id='rating-avg-output', className='card-text nb')
                    ], className='card-body')
                ],className='card border-primary mb-3'),

                html.Div([
                    html.Div([
                        'Rating median'
                    ], className='card-header'),
                    html.Div([
                        html.P(id='rating-median-output', className='card-text nb')
                    ], className='card-body')
                ],className='card border-primary mb-3'),
            ], className='card-container'),

            html.Div([
                dcc.Loading(
                    id="loading-graph",
                    children=[
                        dcc.Graph(id='rating-distribution-output')
                    ],
                    type="circle"
                )
            ]),

            html.Section([

                html.P("List of hotels ranked and based on their stars within each city",
                    className='fw-bold'
                ),

                html.Div([
                    html.P('City :'),
                    html.Div(
                        dcc.Dropdown(id='city-dropdown',
                                    placeholder="Select a city"
                        ),
                        className='dropdown-city'
                    ),
                ], className='dropdown-container'),

                dcc.Loading(
                    id="loading-graph",
                    children=[
                        dash_table.DataTable(id='city-output-div', columns=[], data=[])
                    ],
                    type="circle"
                )
            ]),


            html.Section([

                html.P("List of regions ranked by hotel capacity",
                    className='fw-bold'
                ),

                html.Div([
                    html.P('Top :'),
                    html.Div(
                        dcc.Dropdown(id='top-capacity-dropdown',
                                    placeholder="Select a value",
                                    options=rank_options
                        ),
                        className='dropdown-rank'
                    ),
                ], className='dropdown-container'),

                dcc.Loading(
                    id="loading-graph",
                    children=[
                        dash_table.DataTable(id='top-capacity-output-div', columns=[], data=[])
                    ],
                    type="circle"
                )
            ]),


            html.Section([

                html.P("List of regions ranked by hotel count who star rating above national average",
                    className='fw-bold'
                ),

                html.Div([
                    html.P('Top :'),
                    html.Div(
                        dcc.Dropdown(id='top-avg-dropdown',
                                    placeholder="Select a value",
                                    options=rank_options
                        ),
                        className='dropdown-rank'
                    ),
                ], className='dropdown-container'),

                dcc.Loading(
                    id="loading-graph",
                    children=[
                        dash_table.DataTable(id='top-avg-output-div', columns=[], data=[])
                    ],
                    type="circle"
                )
            ])

        ], className='view-container')
    ])



    return layout
