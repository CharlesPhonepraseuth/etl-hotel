# Standard library imports
import os
import json
import shutil
from typing import Dict, Optional, Union

# Third party imports
import polars as pl


def remove_files(folder: str) -> bool:
    """This function remove all files into specific folder

    Args:
        folder (str): folder path to clean

    Returns:
        bool: True or False
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            return False
    
    print(f"The folder {folder} is clean")
    return True


def get_data_schema(source: str) -> dict:
    """This function get data schema from config file depends on source

    Args:
        source (str): source from config file

    Returns:
        dict: data schema
    """
    with open('config/data_schema.json', 'r') as schema_file:
        data_schema = json.load(schema_file)

    schema = {
        col_name: getattr(pl, dtype) for col_name, dtype in data_schema[source].items()
    }

    return schema


def get_db_creds() -> Dict[str, Optional[Union[str, int]]]:
    return {
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'db': os.getenv("POSTGRES_DB"),
        'host': os.getenv("POSTGRES_HOST"),
        'port': int(os.getenv("POSTGRES_HTTP_PORT", 5432)),
    }
