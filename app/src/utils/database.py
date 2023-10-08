# Standard library imports
from typing import Union, Dict, Any

# Third party imports
import pandas as pd
import polars as pl
from sqlalchemy import create_engine, text

# Local application imports
from src.utils import helper


class DatabaseConnection:
    def __init__(self, db: str, user: str, password: str, host: str, port: int):
        self.conn_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'
        self.engine = create_engine(self.conn_url)

    def get_all_table(self, table_name: str, output_format="pd") -> Union[pd.DataFrame, pl.DataFrame]:
        """This function get all data from specific table

        Args:
            table_name (str): table name to fetch
            output_format (str, optional): type of dataframe wanted. Defaults to "pd".

        Returns:
            Union[pd.DataFrame, pl.DataFrame]: data into dataframe
        """
        try:
            df = pd.read_sql_table(table_name, con=self.engine)
            df = self.__get_pd_or_pl(df, output_format)
            
            return df
        except Exception as e:
            print("An error occured while fetching data :", str(e))
    
    def read_sql(self, query: str, output_format="pd") -> Union[pd.DataFrame, pl.DataFrame]:
        """This function read sql query and return data as dataframe

        Args:
            query (str): sql query
            output_format (str, optional): type of dataframe wanted. Defaults to "pd".

        Returns:
            Union[pd.DataFrame, pl.DataFrame]: data into dataframe
        """
        try:
            df = pd.read_sql_query(query, con=self.engine)
            df = self.__get_pd_or_pl(df, output_format)

            return df
        except Exception as e:
            print("An error occured while fetching data :", str(e))
    
    def execute_sql_file(self, file_path: str, params={}, output_format="json") -> Union[Dict[str, Any], pd.DataFrame, pl.DataFrame]:
        """This function execute sql file and return response

        Args:
            file_path (str): sql script file path
            params (dict, optional): parameter for sql placeholder. Defaults to {}.
            output_format (str, optional): output format (json, pd, pl). Defaults to "json".

        Returns:
            Union[Dict[str, Any], pd.DataFrame, pl.DataFrame]: json response for api. pd or pl dataframe.
        """
        try:
            query = helper.load_query(file_path)

            if output_format == "json":

                with self.engine.connect() as conn:
                    if not params:
                        result = conn.execute(text(query))
                    else:
                        result = conn.execute(text(query), params)
                    
                    result_json = result.mappings().all()

                    return result_json
            else:

                if not query:
                    return pd.DataFrame()

                if not params:
                    df = pd.read_sql_query(query, con=self.engine)
                else:
                    df = pd.read_sql_query(query, params=params, con=self.engine)
                
                df = self.__get_pd_or_pl(df, output_format)
                
                return df
        except Exception as e:
            print("An error occured while executing sql file :", str(e))

    def __get_pd_or_pl(self, df: pd.DataFrame, output_format: str) -> Union[pd.DataFrame, pl.DataFrame]:
        """This function allow us to keep pandas dataframe or turn it into polars

        Args:
            df (pd.DataFrame): pandas dataframe
            output_format (str): type of dataframe wanted

        Raises:
            ValueError: output format not allowed

        Returns:
            Union[pd.DataFrame, pl.DataFrame]: pandas or polars dataframe
        """
        if output_format == "pd":
            return df
        elif output_format == "pl":
            return pl.DataFrame(df)
        else:
            raise ValueError("Invalid output_format. Use 'pd' or 'pl'.")

    def insert_pl_to_db(self, table_name: str, df: pl.DataFrame) -> None:
        """This function insert polars dataframe into database

        Args:
            table_name (str): table name to insert 
            df (pl.DataFrame): polars dataframe to insert
        """
        try:
            df.write_database(table_name, self.conn_url, if_exists="append", engine="sqlalchemy")
        except Exception as e:
            print("An error occured while inserting data :", str(e))
    
    def insert_if_not_exists(self, df_to_insert: pd.DataFrame, table_name: str) -> None:
        """This function insert data who is not already into database (idempotent)

        Args:
            df_to_insert (pd.DataFrame): pandas dataframe to insert
            table_name (str): table name to insert
        """
        try:
            df_pd_from_db = self.get_all_table(table_name)

            anti_join = df_to_insert.merge(df_pd_from_db, how='outer', indicator=True)
            anti_join_result = anti_join[anti_join['_merge'] == 'left_only'].drop(['id', '_merge'], axis=1)

            df_final_to_insert = pl.from_pandas(anti_join_result)

            self.insert_pl_to_db(table_name, df_final_to_insert)

        except Exception as e:
            print("An error occured while inserting data :", str(e))
