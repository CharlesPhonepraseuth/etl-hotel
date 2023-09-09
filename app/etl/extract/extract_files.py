# Standard library imports
import os
import gzip
import shutil

# Third party imports
from bs4 import BeautifulSoup as bs
import wget
import requests

# Local application imports
from src.utils import helper, decorators
from src.validation import checks


@decorators.time_func
def get_hotel_csv(folder_path: str) -> bool:
    """This function extract french hotels csv file

    Args:
        folder_path (str): folder path of files to check

    Returns:
        bool: True or False
    """
    try:
        hotel_url = 'https://www.data.gouv.fr/fr/datasets/hebergements-collectifs-classes-en-france/'

        if checks.is_link_reachable(hotel_url) == True:
            page = requests.get(hotel_url)
            soup = bs(page.content, features='html.parser')

            links = soup.find_all("a", attrs={'title': 'Télécharger la ressource'})
            data_link = links[1]['href']

            # we have to rename the file
            new_filename = 'hebergements-collectifs-classes-en-france.csv'

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # remove file before load new one
            helper.remove_files(folder_path)
            file_path = folder_path + new_filename

            wget.download(data_link, out=file_path)
            print(f"The file '{new_filename}' was successfully downloaded")

            return True
        
    except Exception as e:
        print("An error occured :", str(e))
        return False


@decorators.time_func
def get_adress_csv(folder_path: str) -> bool:
    """This function extract adress csv files from gz files

    Args:
        folder_path (str): folder path of files to check

    Returns:
        bool: True or False
    """
    try:
        adresse_url = 'https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/'
        
        if checks.is_link_reachable(adresse_url) == True:
            # we remove firstly all adress files
            gz_path = folder_path + "gz/"
            csv_path = folder_path + "csv/"
            places_path = csv_path + "places/"
            streets_path = csv_path + "streets/"
            
            if os.path.exists(folder_path):
                helper.remove_files(folder_path)

            folders = [folder_path, gz_path, csv_path, places_path, streets_path]

            # then we create folders
            for folder in folders:
                if not os.path.exists(folder):
                    os.makedirs(folder)

            page = requests.get(adresse_url)
            soup = bs(page.content, features="html.parser")
            links = soup.find_all("a")

            for a in links:
                filename = a["href"]

                if not ("../" in filename or "adresses-france" in filename):
                    link = adresse_url + filename

                    if not checks.is_gz_file_empty_from_link(link):
                        wget.download(link, out=gz_path)

                        # we open .gz file to download .csv file
                        with gzip.open(gz_path + filename, 'rb') as f_in:
                            filename_without_ext = filename.replace(".gz", "")
                            # adresses and lieux-dits don't have same schema
                            # to handle it easily, we separate into 2 folder
                            if "adresses" in filename:
                                path = streets_path
                            elif "lieux-dits" in filename:
                                path = places_path
                                
                            with open(path + filename_without_ext, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                                print(f"{filename_without_ext} successfully created")

                        # clean memory usage
                        del f_in
                        del f_out
                else:
                    pass
            
            # we remove .gz files to keep the project clean and lighter
            helper.remove_files(gz_path)
            
            return True

    except Exception as e:
        print("An error occured :", str(e))
        return False

