# Third party imports
import pytest

# Local application imports
from src.validation import checks


@pytest.mark.parametrize(
    "link, expected_result",
    [
        ("https://www.google.com", True),
        ("https://www.link_not_exist.com", False)
    ]
)
def test_is_link_reachable(link: str, expected_result: bool):
    is_valid = checks.is_link_reachable(link)

    assert is_valid is expected_result


@pytest.mark.parametrize(
    "filename, expected_result",
    [
        ("lieux-dits-989-beta.csv.gz", True), # empty file
        ("lieux-dits-01-beta.csv.gz", False) # not empty file
    ]
)
def test_is_gz_file_empty_from_link(filename: str, expected_result: bool):
    basepath = "https://adresse.data.gouv.fr/data/ban/adresses/2023-08-09/csv/"
    is_empty = checks.is_gz_file_empty_from_link(basepath + filename)

    assert is_empty is expected_result


@pytest.mark.parametrize(
    "filename, expected_result",
    [
        ("empty_file.csv", True),
        ("not_empty_file.csv", False)
    ]
)
def test_csv_file_is_empty(filename: str, expected_result: bool):
    basepath = "/app/tests/test_files/"
    is_empty = checks.is_csv_file_empty(basepath + filename)

    assert is_empty is expected_result
