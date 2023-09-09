# Third party imports
import polars as pl

# Local application imports
from src.utils import helper


def test_get_transform_schema():
    expected_schema = {
        "name":         pl.Utf8,
        "room":         pl.Int64,
        "capacity":     pl.Int64,
        "adress":       pl.Utf8,
        "zip":          pl.Utf8,
        "city":         pl.Utf8,
        "star":         pl.Int64,
        "date":         pl.Utf8,
        "day":          pl.Int64,
        "month":        pl.Int64,
        "year":         pl.Int64,
        "latitude":     pl.Float64,
        "longitude":    pl.Float64,
        "x":            pl.Float64,
        "y":            pl.Float64,
        "concat":       pl.Utf8
    }

    transform_schema = helper.get_data_schema("transform")

    assert transform_schema == expected_schema

