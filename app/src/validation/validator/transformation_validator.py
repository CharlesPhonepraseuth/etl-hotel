# Third party imports
import polars as pl

# Local application imports
from src.utils import helper
from src.validation.validator.dataframe_validator import DataFrameValidator


class TransformationValidator(DataFrameValidator):
    def __init__(self, df: pl.DataFrame):
        super().__init__(df)
        self.expected_schema = helper.get_data_schema("transform")
    
    def is_values_valid(self):
        """This function check if dataframe haven't got null values

        Returns:
            bool: True or False
        """
        columns_with_nulls = [col for col in self.df.columns if self.df[col].is_null().any()]

        if len(columns_with_nulls) > 0:
            print("Columns with null values:", columns_with_nulls)
            return False

        return True
    
    def is_date_cross_field_valid(self) -> bool:
        """This function check if columns related to date is correct

        Returns:
            bool: True or False
        """
        df = self.df.with_columns(
                    pl.date(self.df['year'], self.df['month'], self.df['day']) \
                    .alias('concatenated_date')
            )

        wrong_date_df = df.filter(df['concatenated_date'] != df['date']) \
                          .select(["date", "year", "month", "day", "concatenated_date"])

        if not wrong_date_df.is_empty():
            print("Concatenated date is not equal to date:", wrong_date_df)
            return False

        return True

    def validate(self) -> bool:
        """This function apply multiple validation

        Returns:
            bool: True or False
        """
        is_valid = (
            super().validate()
            and self.is_columns_valid()
            and super().is_date_range_valid("%Y-%m-%d")
            and self.is_date_cross_field_valid()
        )

        return is_valid
