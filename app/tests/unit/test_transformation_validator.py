# Third party imports
import pytest
import polars as pl

# Local application imports
from src.validation.validator.transformation_validator import TransformationValidator


@pytest.mark.parametrize(
    "dataframe, method_name, expected_result",
    [
        ("processed_df", "is_columns_valid", True),
        ("processed_df", "is_schema_valid", True),
        ("processed_df", "is_values_valid", True),
        ("processed_df", "is_date_cross_field_valid", True),
        ("processed_df", "is_date_range_valid", True),
        ("processed_df", "validate", True),
        ("invalid_processed_df", "is_columns_valid", False),
        ("invalid_processed_df", "is_schema_valid", False),
        ("invalid_processed_df", "is_values_valid", False),
        ("invalid_processed_df", "is_date_cross_field_valid", False),
        ("invalid_processed_df", "is_date_range_valid", False),
        ("invalid_processed_df", "validate", False)
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

    validator = TransformationValidator(dataframe)
    method = getattr(validator, method_name)
    is_valid = method("%Y-%m-%d") if method_name == "is_date_range_valid" else method()

    assert is_valid is expected_result
