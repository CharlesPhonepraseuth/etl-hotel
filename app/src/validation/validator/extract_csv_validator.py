# Third party imports
import polars as pl

# Local application imports
from src.utils import helper
from src.validation.validator.dataframe_validator import DataFrameValidator


class ExtractCSVValidator(DataFrameValidator):
    def __init__(self, df: pl.DataFrame, source_name: str):
        super().__init__(df)
        self.source_name = source_name

        if "hebergements" in source_name:
            self.expected_schema = helper.get_data_schema("accommodations")
        elif "lieux-dits" in source_name:
            self.expected_schema = helper.get_data_schema("places")
        elif "adresses" in source_name:
            self.expected_schema = helper.get_data_schema("streets")
        else:
            raise ValueError("Invalid source_name")

    def validate(self) -> bool:
        """This function apply multiple validation

        Returns:
            bool: True or False
        """
        if "hebergement" in self.source_name:
            is_valid = (
                super().validate()
                and super().is_date_range_valid("%d/%m/%Y")
            )
        elif any(item in self.source_name for item in ["lieux-dits", "adresses"]):
            is_valid = super().validate()

        return is_valid
