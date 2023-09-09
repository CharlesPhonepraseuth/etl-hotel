# Third party imports
import pytest
import polars as pl

# Local application imports
from src.data.data_preprocessing import preprocess_hotel, preprocess_adress


@pytest.mark.parametrize(
    "dataframe, processed_dataframe, source, expected_result",
    [
        ("places_df", "processed_places_df", "places", True),
        ("places_df", "invalid_processed_places_df", "places", False),
        ("streets_df", "processed_streets_df", "streets", True),
        ("streets_df", "invalid_processed_streets_df", "streets", False)
    ]
)
def test_preprocess_adress(request: pytest.FixtureRequest, dataframe: pl.LazyFrame, processed_dataframe: pl.DataFrame, source: str, expected_result: bool):
    dataframe = request.getfixturevalue(dataframe)
    dataframe = preprocess_adress(dataframe, source)

    processed_dataframe = request.getfixturevalue(processed_dataframe)

    assert dataframe.frame_equal(processed_dataframe) is expected_result


@pytest.mark.parametrize(
    "dataframe, processed_dataframe, expected_result",
    [
        ("accommodation_df", "processed_accommodation_df", True),
        ("accommodation_df", "invalid_processed_accommodation_df", False)
    ]
)
def test_preprocess_accommodation(request: pytest.FixtureRequest, dataframe: pl.LazyFrame, processed_dataframe: pl.DataFrame, expected_result: bool):
    dataframe = request.getfixturevalue(dataframe)
    dataframe = preprocess_hotel(dataframe)

    processed_dataframe = request.getfixturevalue(processed_dataframe)

    assert dataframe.frame_equal(processed_dataframe) is expected_result


