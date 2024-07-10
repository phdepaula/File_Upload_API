import os

import pandas as pd

from src.util.error_generator import ErrorGenerator
from src.util.pandas_handler import PandasHandler


def test_reading_csv_correctly():
    """
    Method to teste if csv file is being readed.
    """
    file_path = os.path.join(os.getcwd(), "assets", "input.csv")
    separator = ","
    data_type = {
        "name": str,
        "governmentId": str,
        "email": str,
        "debtAmount": str,
        "debtDueDate": str,
        "debtId": str,
    }

    pandas_handler = PandasHandler(file_path)
    pandas_handler.read_csv(separator, data_type)

    dataframe = pandas_handler.dataframe

    assert isinstance(dataframe, pd.DataFrame)


def test_reading_csv_with_error():
    """
    Method to teste if csv file is being readed.
    """
    file_path = os.path.join(os.getcwd(), "assets", "in.csv")
    separator = ","
    data_type = {
        "name": str,
        "governmentId": str,
        "email": str,
        "debtAmount": str,
        "debtDueDate": str,
        "debtId": str,
    }

    pandas_handler = PandasHandler(file_path)

    error_code = 0

    try:
        pandas_handler.read_csv(separator, data_type)
    except ErrorGenerator as error:
        error_code = error.error_code

    assert error_code == 1
