# Third party imports
import plotly.express as px
from dash.dependencies import Output, Input

# Local application imports
from data_mapper import DataMapper


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
            mapper = DataMapper()
            df = mapper.get_hotel_count()
            
            return df["value"]


    @app.callback(
        Output('rating-avg-output', 'children'),
        [Input('url', 'pathname')]
    )
    def update_rating_avg_output(pathname):

        if pathname == '/hotel-analysis':
            mapper = DataMapper()
            df = mapper.get_national_rating_avg()
            
            return df["value"]


    @app.callback(
        Output('rating-median-output', 'children'),
        [Input('url', 'pathname')]
    )
    def update_rating_median_output(pathname):

        if pathname == '/hotel-analysis':
            mapper = DataMapper()
            df = mapper.get_rating_median()
            
            return df["value"]
        

    @app.callback(
        Output('rating-distribution-output', 'figure'),
        [Input('url', 'pathname')]
    )
    def update_rating_distribution_output(pathname):

        if pathname == '/hotel-analysis':
            mapper = DataMapper()
            df = mapper.get_star_distribution()

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
            mapper = DataMapper()
            df = mapper.get_all_cities()

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

        param = {"city": city}

        mapper = DataMapper()
        df = mapper.get_hotel_rank_by_city(param)

        columns = [{'name': col, 'id': col} for col in df.columns]
        data = df.to_dict('records')

        return columns, data
    

    @app.callback(
        Output('top-capacity-output-div', 'columns'),
        Output('top-capacity-output-div', 'data'),
        [Input(component_id = 'top-capacity-dropdown', component_property = 'value')]
    )
    def update_rank_hotel_list_by_capacity_output(rank):

        param = {"rank": rank}

        mapper = DataMapper()
        df = mapper.get_hotel_rank_by_capacity(param)

        columns = [{'name': col, 'id': col} for col in df.columns]
        data = df.to_dict('records')

        return columns, data
    

    @app.callback(
        Output('top-avg-output-div', 'columns'),
        Output('top-avg-output-div', 'data'),
        [Input(component_id = 'top-avg-dropdown', component_property = 'value')]
    )
    def update_rank_hotel_count_by_avg_output(rank):

        param = {"rank": rank}

        mapper = DataMapper()
        df = mapper.get_hotel_count_and_rank_per_region_above_avg_rating(param)

        columns = [{'name': col, 'id': col} for col in df.columns]
        data = df.to_dict('records')

        return columns, data
    