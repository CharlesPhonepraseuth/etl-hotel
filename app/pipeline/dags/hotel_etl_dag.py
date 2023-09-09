# Standard library imports
import os

# Third party imports
from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

# Local application imports
from etl.extract import extract_files
from etl.transform import transform_files
from etl.load import load_files
from src.validation import data_validation


DATA_FOLDER = os.environ.get("DATA_FOLDER", "/opt/airflow/data/")


with DAG("hotel_ETL_dag",
         tags=["etl", "hotel"],
         schedule_interval=None,
         default_args={
             "owner": "airflow",
             "start_date": days_ago(0, minute=1)
         },
         catchup = False) as dag:
    
    @task
    def extract_hotel():
        folder_path = DATA_FOLDER + "external/accommodations/"
        # extract_files.get_hotel_csv(folder_path)

        is_valid = data_validation.validate(folder_path, "accommodations")

        if not is_valid:
            raise ValueError("Extract hotel not valid")

    
    @task
    def extract_adress():
        folder_path = DATA_FOLDER + "external/adress/"
        # extract_files.get_adress_csv(folder_path)

        is_valid = data_validation.validate(folder_path + "csv/", "adress")

        if not is_valid:
            raise ValueError("Extract adress not valid")

    @task
    def transform():
        folder_path = DATA_FOLDER
        # transform_files.merge_csv(folder_path)
        
        folder_path = DATA_FOLDER + "processed/"
        is_valid = data_validation.validate(folder_path, "transform")

        if not is_valid:
            raise ValueError("Transform not valid")
    
    @task
    def load():
        folder_path = DATA_FOLDER + "processed/"
        load_files.load(folder_path)
    

    [extract_hotel(), extract_adress()]  >> transform() >> load()
