import os
from typing import List

from src.util.error_generator import ErrorGenerator


class Invoice_Database:
    """
    Class to create database to save invoices generated.
    """

    DATABASE_NAME = "invoice_database.txt"

    def __init__(self) -> None:
        self.database_path = self._get_database_path()

    def create_database_file(self, content: List) -> None:
        """
        Method to create invoice database.
        """
        try:
            text = "\n".join(content)

            if os.path.exists(self.database_path):
                text = "\n" + text

            with open(self.database_path, "a") as file:
                file.write(text)
        except Exception as error:
            raise ErrorGenerator(4, f"Error creating database: {error}")

    def _get_database_path(self) -> str:
        """
        Method to get database path
        """
        directory_path = os.path.join(os.getcwd(), "src", "database", "file")

        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        database_path = os.path.join(directory_path, self.DATABASE_NAME)

        return database_path

    def get_all_data(self) -> List:
        """
        Method to get all dbt_id registred.
        """
        try:
            if not os.path.exists(self.database_path):
                return []
            else:
                with open(self.database_path, "r") as file:
                    content = file.read()
                    return content.split("\n")
        except Exception as error:
            raise ErrorGenerator(5, f"Error getting all data: {error}")
