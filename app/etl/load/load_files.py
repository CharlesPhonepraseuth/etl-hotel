# Third party imports
import polars as pl
from sqlalchemy.exc import OperationalError

# Local application imports
from src.utils import helper, decorators
from src.utils.database import DatabaseConnection


@decorators.time_func
def load(folder_path: str) -> bool:
    """This function load clean dataframe into multiple tables

    Args:
        folder_path (str): folder path of files to check

    Returns:
        bool: True or False
    """
    try:
        connection = DatabaseConnection(**helper.get_db_creds())

        custom_dtypes = helper.get_data_schema("transform")
        filename = "preprocessed_data.csv"

        df = pl.read_csv(folder_path + filename,
                         separator=";",
                         dtypes=custom_dtypes)


        # handle dim_adress table
        adress_table = "dim_adress"
        adress_columns = ["adress", "zip", "city", "concat"]

        adress_to_insert = df.select(adress_columns) \
                             .unique(subset=adress_columns, keep="first") \
                             .to_pandas()

        connection.insert_if_not_exists(adress_to_insert, adress_table)

        # handle dim_location table
        location_table = "dim_location"
        location_columns = ["longitude", "latitude", "x", "y"]

        location_to_insert = df.select(location_columns) \
                               .unique(subset=location_columns, keep="first") \
                               .to_pandas()

        connection.insert_if_not_exists(location_to_insert, location_table)

        # handle dim_info table
        info_table = "dim_info"
        info_columns = ["name", "room", "capacity"]

        info_to_insert = df.select(info_columns) \
                           .unique(subset=info_columns, keep="first") \
                           .to_pandas()

        connection.insert_if_not_exists(info_to_insert, info_table)

        # handle dim_date table
        date_table = "dim_date"
        date_columns = ["date", "day", "month", "year"]

        date_to_insert = df.select(date_columns) \
                           .unique(subset=date_columns, keep="first") \
                           .to_pandas()
        
        connection.insert_if_not_exists(date_to_insert, date_table)

        # handle fact_hotel table
        pl_adress_db = connection.get_all_table(adress_table, "pl") \
                                 .rename({"id":"adress_id"})
        
        pl_location_db = connection.get_all_table(location_table, "pl") \
                                   .rename({"id":"location_id"})
        
        pl_info_db = connection.get_all_table(info_table, "pl") \
                               .rename({"id":"info_id"})
        
        pl_date_db = connection.get_all_table(date_table, "pl") \
                               .rename({"id":"date_id"})
        
        df = df.join(pl_adress_db, on=adress_columns) \
               .join(pl_location_db, on=location_columns) \
               .join(pl_info_db, on=info_columns) \
               .join(pl_date_db, on=date_columns)
        
        hotel_table = "fact_hotel"
        hotel_to_insert = df.select(["info_id", "adress_id", "location_id", "date_id", "star"]) \
                            .to_pandas()

        connection.insert_if_not_exists(hotel_to_insert, hotel_table)

        return True

    except OperationalError as e:
        print("Database connection failed: ", e)
        return False
    except Exception as e:
        print("An error occurred while deleting tables: ", e)
        return False