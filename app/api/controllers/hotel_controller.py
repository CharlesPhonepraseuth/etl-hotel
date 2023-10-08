# Local application imports
from data_mapper import DataMapper


def get_hotel_count():
    result = DataMapper().get_hotel_count()
    return result

def get_rating_average():
    result = DataMapper().get_rating_average()
    return result

def get_rating_median():
    result = DataMapper().get_rating_median()
    return result

def get_rating_distribution():
    result = DataMapper().get_rating_distribution()
    return result

def get_all_cities():
    result = DataMapper().get_all_cities()
    return result

def get_hotel_rank_by_city(name: str):
    param = {"city": name}
    result = DataMapper().get_hotel_rank_by_city(param)
    return result

def get_hotel_rank_by_capacity(nb: int):
    param = {"rank": int(nb)}
    result = DataMapper().get_hotel_rank_by_capacity(param)
    return result

def get_hotel_count_and_rank_per_region_above_avg_rating(nb: int):
    param = {"rank": int(nb)}
    result = DataMapper().get_hotel_count_and_rank_per_region_above_avg_rating(param)
    return result
