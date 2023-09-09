# Standard library imports
import csv

# Third party imports
import requests


def is_link_reachable(url: str) -> bool:
    """This function check if the url is reachable

    Args:
        url (str): url to check

    Returns:
        bool: True or False
    """
    try:
        response = requests.head(url, timeout=10)
        if response.status_code == 200:
            print(f"The link {url} is reachable")
            return True
        else:
            print(f"The link {url} is not reachable (status code : {response.status_code})")
            return False
    except requests.exceptions.RequestException as e:
        print("An error occured on checking {}. Reason: {}".format(url, e))
        return False


def is_gz_file_empty_from_link(link: str) -> bool:
    """This function check if gz file from link is empty

    Args:
        link (str): link to check if gz file is empty

    Returns:
        bool: True or False
    """
    response = requests.head(link)
    content_length = int(response.headers.get('Content-Length', 0))
    # strangely, content-length is equal 20 when empty
    return content_length <= 20
    
    
def is_csv_file_empty(file_path: str) -> bool:
    """This function check if the csv file is empty

    Args:
        file_path (str): file path to check

    Returns:
        bool: True or False
    """
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        # Check if the file has any rows of data
        return not any(row for row in reader)
