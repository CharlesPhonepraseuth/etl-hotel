# Local application imports
from data_mapper import DataMapper
from api_helper import json_to_api_response


def handle_undefined_endpoint(undefined_endpoint: str):
    print(undefined_endpoint)
    result = json_to_api_response(None)
    return result

def get_hotel_count():
    json_data = DataMapper().get_hotel_count()
    result = json_to_api_response(json_data)
    return result

def get_rating_average():
    json_data = DataMapper().get_rating_average()
    result = json_to_api_response(json_data)
    return result

def get_rating_median():
    json_data = DataMapper().get_rating_median()
    result = json_to_api_response(json_data)
    return result

def get_rating_distribution():
    json_data = DataMapper().get_rating_distribution()
    result = json_to_api_response(json_data)
    return result

def get_all_cities():
    json_data = DataMapper().get_all_cities()
    result = json_to_api_response(json_data)
    return result

def get_hotel_rank_by_city(name: str):
    param = {"city": name}
    json_data = DataMapper().get_hotel_rank_by_city(param)
    result = json_to_api_response(json_data)
    return result

def get_hotel_rank_by_capacity(nb: int):
    param = {"rank": int(nb)}
    json_data = DataMapper().get_hotel_rank_by_capacity(param)
    result = json_to_api_response(json_data)
    return result

def get_hotel_count_and_rank_per_region_above_avg_rating(nb: int):
    param = {"rank": int(nb)}
    json_data = DataMapper().get_hotel_count_and_rank_per_region_above_avg_rating(param)
    result = json_to_api_response(json_data)
    return result
