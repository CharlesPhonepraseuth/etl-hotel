# Standard library imports
import os
import time
from pathlib import Path

# Third party imports
import polars as pl

# Local application imports
from src.utils import helper, decorators
from src.validation import checks
from src.validation.validator.extract_csv_validator import ExtractCSVValidator
from src.validation.validator.transformation_validator import TransformationValidator


@decorators.time_func
def validate(folder_path: str, source: str) -> bool:
    """This function apply validations

    Args:
        folder_path (str): folder path of files to check
        source (str): which type of validation use

    Returns:
        bool: True or False
    """
    is_valid_list = []

    if source == "accommodations":
        schema = helper.get_data_schema(source)
        filename = 'hebergements-collectifs-classes-en-france.csv'

        df = pl.read_csv(Path(folder_path + filename),
                            separator=";",
                            encoding="ISO-8859-1",
                            dtypes=schema,
                            null_values=['-'])
        
        validator = ExtractCSVValidator(df, filename)
        is_valid_list.append(validator.validate())

    elif source == "adress":
        for directory in os.listdir(folder_path):
            if directory in ["places", "streets"]:

                schema = helper.get_data_schema(directory)

                dir_path = os.path.join(folder_path, directory)

                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)

                    if os.path.isfile(file_path) and not checks.is_csv_file_empty(file_path):

                        df_adress = pl.scan_csv(file_path,
                                                separator=";",
                                                dtypes=schema) \
                                      .collect()

                        validator = ExtractCSVValidator(df_adress, filename)
                        is_valid_list.append(validator.validate())

    elif source == "transform":
        schema = helper.get_data_schema(source)
        filename = "preprocessed_data.csv"

        df = pl.read_csv(folder_path + filename,
                         separator=";",
                         dtypes=schema)

        validator = TransformationValidator(df)
        is_valid_list.append(validator.validate())

    is_valid = all(is_valid_list)

    print(f'{source} validation status: {is_valid}')

    return is_valid
