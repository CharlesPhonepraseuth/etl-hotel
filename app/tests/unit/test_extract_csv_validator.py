# Third party imports
import pytest
import polars as pl

# Local application imports
from src.validation.validator.extract_csv_validator import ExtractCSVValidator


@pytest.mark.parametrize(
    "dataframe, method_name, expected_result",
    [
        ("accommodation_df", "is_columns_valid", True),
        ("accommodation_df", "is_schema_valid", True),
        ("accommodation_df", "is_date_range_valid", True),
        ("accommodation_df", "validate", True),
        ("invalid_accommodation_df", "is_columns_valid", False),
        ("invalid_accommodation_df", "is_schema_valid", False),
        ("invalid_accommodation_df", "is_date_range_valid", False),
        ("invalid_accommodation_df", "validate", False)
    ]
)
def test_validation_methods(request: pytest.FixtureRequest, dataframe: pl.DataFrame, method_name: str, expected_result: bool):
    """This function test every validation method,
    from indivual methods (isolation) to interaction (orchestration) 

    Args:
        request (pytest.FixtureRequest): A request object gives access to the requesting test context
        dataframe (pl.DataFrame): dataframe to test
        method_name (str): method to test
        expected_result (bool): result expected
    """
    dataframe = request.getfixturevalue(dataframe)

    validator = ExtractCSVValidator(dataframe, "hebergements")
    method = getattr(validator, method_name)
    is_valid = method("%d/%m/%Y") if method_name == "is_date_range_valid" else method()

    assert is_valid is expected_result


# @pytest.mark.parametrize(
#     "dataframe, method_name, expected_result",
#     [
#         ("extract_places_df", "is_columns_valid", True),
#         ("extract_places_df", "is_schema_valid", True),
#         ("extract_places_df", "validate", True),
#         ("invalid_extract_places_df", "is_columns_valid", False),
#         ("invalid_extract_places_df", "is_schema_valid", False),
#         ("invalid_extract_places_df", "validate", False)
#     ]
# )
# def test_validation_methods(request: pytest.FixtureRequest, dataframe: pl.DataFrame, method_name: str, expected_result: bool):
#     """This function test every validation method,
#     from indivual methods (isolation) to interaction (orchestration) 

#     Args:
#         request (pytest.FixtureRequest): A request object gives access to the requesting test context
#         dataframe (pl.DataFrame): dataframe to test
#         method_name (str): method to test
#         expected_result (bool): result expected
#     """
#     dataframe = request.getfixturevalue(dataframe)

#     validator = ExtractCSVValidator(dataframe, "lieux-dits")
#     method = getattr(validator, method_name)
#     is_valid = method()

#     assert is_valid == expected_result

