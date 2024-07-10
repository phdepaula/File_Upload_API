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

    def get_values_from_column(self, column: str) -> List:
        """
        Method to get values from a specific column
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
