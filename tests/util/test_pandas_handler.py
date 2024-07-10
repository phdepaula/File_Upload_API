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
    Method to test if csv file is being readed.
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


def test_get_values_from_column_to_insert():
    """
    Method to test get_values_from_column_to_insert method.
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
    values_top_5 = pandas_handler.get_values_from_column_to_insert("debtId")[
        0:5
    ]

    result_top_5 = [
        ["ea23f2ca-663a-4266-a742-9da4c9f4fcb3"],
        ["acc1794e-b264-4fab-8bb7-3400d4c4734d"],
        ["9f5a2b0c-967e-4443-a03d-9d7cdcb2216f"],
        ["33bec852-beee-477f-ae65-1475c74e1966"],
        ["e2dba21b-5520-4226-82b5-90c6bb3356c6"],
    ]

    assert values_top_5 == result_top_5


def test_get_values_from_column_to_compare():
    """
    Method to test get_values_from_column_to_compare method.
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
    values_top_5 = pandas_handler.get_values_from_column_to_compare("debtId")[
        0:5
    ]

    result_top_5 = [
        "ea23f2ca-663a-4266-a742-9da4c9f4fcb3",
        "acc1794e-b264-4fab-8bb7-3400d4c4734d",
        "9f5a2b0c-967e-4443-a03d-9d7cdcb2216f",
        "33bec852-beee-477f-ae65-1475c74e1966",
        "e2dba21b-5520-4226-82b5-90c6bb3356c6",
    ]

    assert values_top_5 == result_top_5


def test_filter_dataframe():
    """
    Method to test filter_dataframe method.
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
    pandas_handler.filter_dataframe(
        "debtId", ["ea23f2ca-663a-4266-a742-9da4c9f4fcb3"]
    )

    debt_id = pandas_handler.get_values_from_column_to_compare("debtId")
    quantity_of_elements = len(debt_id)

    assert quantity_of_elements == 1
    assert debt_id == ["ea23f2ca-663a-4266-a742-9da4c9f4fcb3"]
