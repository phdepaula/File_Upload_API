from typing import Dict
from src.util.error_generator import ErrorGenerator

import pandas as pd


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
