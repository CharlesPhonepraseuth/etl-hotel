# Standard library imports
from typing import Dict, Any

# Local application imports
from src.utils import helper
from src.utils.database import DatabaseConnection 


BASEPATH = "/code/src/sql_scripts/"


class DataMapper:
    def __init__(self):
        self.conn = DatabaseConnection(**helper.get_db_creds())

    def get_hotel_count(self) -> Dict[str, Any]:
        file_path = BASEPATH + "get_hotel_count.sql"
        result = self.conn.execute_sql_file(file_path)
        return result
    
    def get_rating_average(self) -> Dict[str, Any]:
        file_path = BASEPATH + "get_rating_avg.sql"
        result = self.conn.execute_sql_file(file_path)
        return result

    def get_rating_median(self) -> Dict[str, Any]:
        file_path = BASEPATH + "get_rating_median.sql"
        result = self.conn.execute_sql_file(file_path)
        return result
    
    def get_rating_distribution(self) -> Dict[str, Any]:
        file_path = BASEPATH + "get_rating_distribution.sql"
        result = self.conn.execute_sql_file(file_path)
        return result

    def get_all_cities(self) -> Dict[str, Any]:
        file_path = BASEPATH + "get_all_cities.sql"
        result = self.conn.execute_sql_file(file_path)
        return result

    def get_hotel_rank_by_city(self, param={}) -> Dict[str, Any]:
        file_path = BASEPATH + "get_hotel_rank_by_city.sql"
        result = self.conn.execute_sql_file(file_path, param)
        return result
    
    def get_hotel_rank_by_capacity(self, param={}) -> Dict[str, Any]:
        file_path = BASEPATH + "get_region_rank_by_capacity.sql"
        result = self.conn.execute_sql_file(file_path, param)
        return result
    
    def get_hotel_count_and_rank_per_region_above_avg_rating(self, param={}) -> Dict[str, Any]:
        file_path = BASEPATH + "get_hotel_count_and_rank_per_region_above_avg_rating.sql"
        result = self.conn.execute_sql_file(file_path, param)
        return result
