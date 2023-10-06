# Third party imports
import pandas as pd

# Local application imports
from src.utils import helper
from src.utils.database import DatabaseConnection 


BASEPATH = "/code/src/sql_scripts/"

class DataMapper:
    def __init__(self):
        self.conn = DatabaseConnection(**helper.get_db_creds())

    def get_hotel_count(self) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_hotel_count.sql")
        return df
    
    def get_national_rating_avg(self) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_rating_avg.sql")
        return df

    def get_rating_median(self) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_rating_median.sql")
        return df
    
    def get_star_distribution(self) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_star_distribution.sql")
        return df

    def get_all_cities(self) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_all_cities.sql")
        return df

    def get_hotel_rank_by_city(self, param={}) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_hotel_rank_by_city.sql", param)
        return df
    
    def get_hotel_rank_by_capacity(self, param={}) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_region_rank_by_capacity.sql", param)
        return df
    
    def get_hotel_count_and_rank_per_region_above_avg_rating(self, param={}) -> pd.DataFrame:
        df = self.conn.execute_sql_file(BASEPATH + "get_hotel_count_and_rank_per_region_above_avg_rating.sql", param)
        return df
