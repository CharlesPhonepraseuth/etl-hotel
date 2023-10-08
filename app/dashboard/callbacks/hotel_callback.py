# Standard library imports
import os

# Third party imports
import pandas as pd
import requests
import plotly.express as px
from dash.dependencies import Output, Input


BASE_API_URL = os.environ.get("API_REQUEST_URL", "http://localhost:8000/") + "api/"


def register_callbacks(app):

    ###
    ### callback started when loading view
    ###

    @app.callback(
        Output('hotel-count-output', 'children'),
        [Input('url', 'pathname')]
    )
    def update_hotel_count_output(pathname):

        if pathname == '/hotel-analysis':

            url = BASE_API_URL + "hotel/count"
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            return df["value"]


    @app.callback(
        Output('rating-avg-output', 'children'),
        [Input('url', 'pathname')]
    )
    def update_rating_avg_output(pathname):

        if pathname == '/hotel-analysis':

            url = BASE_API_URL + "rating/average"
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            return df["value"]


    @app.callback(
        Output('rating-median-output', 'children'),
        [Input('url', 'pathname')]
    )
    def update_rating_median_output(pathname):

        if pathname == '/hotel-analysis':

            url = BASE_API_URL + "rating/median"
            response = requests.get(url)
            df = pd.DataFrame(response.json())
            
            return df["value"]
        

    @app.callback(
        Output('rating-distribution-output', 'figure'),
        [Input('url', 'pathname')]
    )
    def update_rating_distribution_output(pathname):

        if pathname == '/hotel-analysis':

            url = BASE_API_URL + "rating/distribution"
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            fig = px.bar(df, x='star', y='frequency', text='frequency', 
                 title='Star Rating Distribution',
                 labels={'star': 'Star Rating', 'frequency': 'Frequency'})
            
            return fig
        

    @app.callback(
        Output(component_id = 'city-dropdown', component_property = 'options'),
        [Input('url', 'pathname')]
    )
    def update_city_dropdown(pathname):

        if pathname == '/hotel-analysis':

            url = BASE_API_URL + "city"
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            city_dropdown_options = [{'label': city.capitalize(), 'value': city} for city in df["city"]]

            return city_dropdown_options


    ###
    ### callback started by user interaction
    ###

    @app.callback(
        Output('city-output-div', 'columns'),
        Output('city-output-div', 'data'),
        [Input(component_id = 'city-dropdown', component_property = 'value')]
    )
    def update_rank_city_list_output(city):

        if city is not None:

            url = BASE_API_URL + "hotel/city/" + city
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            columns = [{'name': col, 'id': col} for col in df.columns]
            data = df.to_dict('records')

            return columns, data
        
        return [], []
    

    @app.callback(
        Output('top-capacity-output-div', 'columns'),
        Output('top-capacity-output-div', 'data'),
        [Input(component_id = 'top-capacity-dropdown', component_property = 'value')]
    )
    def update_rank_hotel_list_by_capacity_output(rank):

        if rank is not None:

            url = BASE_API_URL + "region/rank?nb=" + str(rank)
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            columns = [{'name': col, 'id': col} for col in df.columns]
            data = df.to_dict('records')

            return columns, data
        
        return [], []
    

    @app.callback(
        Output('top-avg-output-div', 'columns'),
        Output('top-avg-output-div', 'data'),
        [Input(component_id = 'top-avg-dropdown', component_property = 'value')]
    )
    def update_rank_hotel_count_by_avg_output(rank):

        if rank is not None:

            url = BASE_API_URL + "region/rating/above-average/rank?nb=" + str(rank)
            response = requests.get(url)
            df = pd.DataFrame(response.json())

            columns = [{'name': col, 'id': col} for col in df.columns]
            data = df.to_dict('records')

            return columns, data
        
        return [], []
    