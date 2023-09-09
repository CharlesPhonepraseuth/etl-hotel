# Standard library imports
import os
from pathlib import Path

# Third party imports
import polars as pl

# Local application imports
from src.utils import helper, decorators
from src.data import data_preprocessing
from src.validation import checks


@decorators.time_func
def merge_csv(folder_path: str) -> bool:
    """This function merge places and adresses csv files into one dataframe to load

    Args:
        folder_path (str): folder path of files to check

    Returns:
        bool: True or False
    """
    try:
        df_clean = pl.DataFrame()

        custom_hotel_dtypes = helper.get_data_schema("accommodations")

        hotel_path = folder_path + "external/accommodations/"
        hotel_filename = "hebergements-collectifs-classes-en-france.csv"

        # use Path to be able to handle ISO-8859-1 encoding
        df_hotel = pl.read_csv(Path(hotel_path + hotel_filename),
                                separator=";",
                                encoding="ISO-8859-1",
                                dtypes=custom_hotel_dtypes,
                                null_values=['-'])

        df_hotel_clean = data_preprocessing.preprocess_hotel(df_hotel)

        adress_path = folder_path + "external/adress/csv/"

        for directory in os.listdir(adress_path):
            if directory in ["places", "streets"]:

                custom_adress_dtypes = helper.get_data_schema(directory)

                dir_path = os.path.join(adress_path, directory)

                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)

                    if os.path.isfile(file_path) and not checks.is_csv_file_empty(file_path):

                        # use LazyFrame due to amount of data larger than available RAM
                        df_adress = pl.scan_csv(file_path,
                                                separator=";",
                                                dtypes=custom_adress_dtypes)

                        df_adress_clean = data_preprocessing.preprocess_adress(df_adress, directory)

                        columns_selected = [
                            "NOM COMMERCIAL",
                            "NOMBRE DE CHAMBRES",
                            "CAPACITÉ D'ACCUEIL (PERSONNES)",
                            "ADRESSE",
                            "CODE POSTAL",
                            "COMMUNE",
                            "CLASSEMENT",
                            "date",
                            "day",
                            "month",
                            "year",
                            "lat",
                            "lon",
                            "x",
                            "y",
                            "concat"
                        ]

                        new_column_names = {
                            "NOM COMMERCIAL":                   "name",
                            "NOMBRE DE CHAMBRES":               "room",
                            "CAPACITÉ D'ACCUEIL (PERSONNES)":   "capacity",
                            "ADRESSE":                          "adress",
                            "CODE POSTAL":                      "zip",
                            "COMMUNE":                          "city",
                            "CLASSEMENT":                       "star",
                            "lat":                              "latitude",
                            "lon":                              "longitude"
                        }

                        df_join = df_hotel_clean.join(df_adress_clean, on="concat", how="inner") \
                                                .select(columns_selected) \
                                                .rename(new_column_names) \
                                                .drop_nulls()
                        
                        df_clean = pl.concat([df_clean, df_join])

        processed_path = folder_path + "processed/"
        result_filename = "preprocessed_data.csv"
  
        if not os.path.exists(processed_path):
            os.makedirs(processed_path)
        
        df_clean.write_csv(processed_path + result_filename, separator=";")

        return True

    except Exception as e:
        print("Une erreur s'est produite :", str(e))
        return False