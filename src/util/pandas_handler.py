from typing import Dict, List

import pandas as pd

from src.util.error_generator import ErrorGenerator


class PandasHandler:
    """
    Class to use lib pandas.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.dataframe = None

    def read_csv(self, separator: str, data_type: Dict) -> None:
        """
        method responsible for reading a csv.
        """
        try:
            self.dataframe = pd.read_csv(
                self.file_path, sep=separator, dtype=data_type
            )
        except Exception as error:
            raise ErrorGenerator(1, f"Error reading csv: {error}")

    def filter_dataframe(self, column: str, values: List) -> None:
        """
        Method to filter dataframe based
        in a condition.
        """
        try:
            self.dataframe = self.dataframe[
                self.dataframe[column].isin(values)
            ]
        except Exception as error:
            raise ErrorGenerator(12, f"Error filtering dataframe: {error}")

    def get_dataframe_values(self) -> List:
        """
        Method to get dataframe values
        """
        try:
            values = self.dataframe.values.tolist()
            return values
        except Exception as error:
            raise ErrorGenerator(
                13, f"Error getting dataframe values: {error}"
            )

    def get_values_from_column_to_compare(self, column: str) -> List:
        """
        Method to get values from a specific column to
        compare
        """
        try:
            if self.dataframe is not None:
                values = (
                    self.dataframe[column].apply(lambda value: value).tolist()
                )
                return values
        except Exception as error:
            raise ErrorGenerator(
                11, f"Error getting values from {column}: {error}"
            )

    def get_values_from_column_to_insert(self, column: str) -> List:
        """
        Method to get values from a specific column to insert
        """
        try:
            if self.dataframe is not None:
                values = (
                    self.dataframe[column]
                    .apply(lambda value: [value])
                    .tolist()
                )
                return values
        except Exception as error:
            raise ErrorGenerator(
                10, f"Error getting values from {column}: {error}"
            )
