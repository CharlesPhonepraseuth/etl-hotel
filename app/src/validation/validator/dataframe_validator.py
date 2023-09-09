# Standard library imports
from datetime import datetime

# Third party imports
import polars as pl


class DataFrameValidator:
    def __init__(self, df: pl.DataFrame):
        self.df = df
        self.expected_schema = {}

    def is_columns_valid(self) -> bool:
        """This function check if columns fit as expected

        Returns:
            bool: True or False
        """
        missing_columns = set(self.expected_schema.keys()) - set(self.df.columns)

        if missing_columns:
            print(f"Missing columns: {', '.join(missing_columns)}")
            return False

        return True

    def is_schema_valid(self) -> bool:
        """This function check if dataframe have good datatype

        Returns:
            bool: True or False
        """
        different_datatype = [key for key, value in self.expected_schema.items() if value != self.df.schema.get(key)]

        if len(different_datatype) > 0:
            print("Keys with different datatypes:", different_datatype)
            return False
        
        return True
    
    def is_date_range_valid(self, fmt: str) -> bool:
        """This function check if date is real range

        Args:
            fmt (str): date format input

        Returns:
            bool: True or False
        """
        min_date_str = "2000-01-01"
        min_date = datetime.strptime(min_date_str, "%Y-%m-%d").date()
        current_date = datetime.now().date()

        # "DATE DE CLASSEMENT" come from accommodations instead of "date" with transformation
        date_col = "DATE DE CLASSEMENT" if fmt == "%d/%m/%Y" else "date" if "%Y-%m-%d" else None

        df = self.df.with_columns(
                        pl.col(date_col).str.strptime(pl.Date, format=fmt)
                          .cast(pl.Utf8)
                          .alias("date")
        )

        date_outside_range_df = df.filter((df["date"] < min_date) | (df["date"] > current_date)) \
                                  .select("date")

        if not date_outside_range_df.is_empty():
            print("Dataframe contains dates outside the valid range:", date_outside_range_df)
            return False

        return True

    def validate(self) -> bool:
        """This function apply multiple validation

        Returns:
            bool: True or False
        """
        is_valid = (
            self.is_columns_valid()
            and self.is_schema_valid()
        )

        return is_valid
