import os
import sqlite3
from typing import List

from src.util.error_generator import ErrorGenerator


class Invoice_Database:
    """
    Class to create database to save invoices generated.
    """

    DATABASE_NAME = "Invoice_Database.db"
    TABLE_INVOICE = "Invoice"
    DEBT_ID = "debt_id"

    def __init__(self) -> None:
        self.database_path = self._get_database_path()
        self._create_database_environment()

    def _create_database_environment(self) -> None:
        """
        Method to create invoice database.
        """
        try:
            connection = self._get_connection()
            cursor = connection.cursor()

            table_query = (
                f"CREATE TABLE IF NOT EXISTS {self.TABLE_INVOICE} "
                + f"({self.DEBT_ID} TEXT PRIMARY KEY)"
            )
            cursor.execute(table_query)

            index_query = (
                f"CREATE INDEX IF NOT EXISTS idx_debt_id ON {self.TABLE_INVOICE}"
                + f" ({self.DEBT_ID})"
            )
            cursor.execute(index_query)

            connection.commit()
            connection.close()
        except Exception as error:
            raise ErrorGenerator(4, f"Error creating database: {error}")

    def _get_connection(self) -> sqlite3.connect:
        """
        Method to get database connection.
        """
        return sqlite3.connect(self.database_path)

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
        Method to get all data registred.
        """
        try:
            connection = self._get_connection()
            cursor = connection.cursor()

            select_query = f"SELECT * FROM {self.TABLE_INVOICE}"
            cursor.execute(select_query)
            data = cursor.fetchall()

            connection.close()

            return list([debt_id[0] for debt_id in data])
        except Exception as error:
            raise ErrorGenerator(5, f"Error getting database data: {error}")

    def insert_content(self, content: List) -> None:
        """
        Method to insert content into Table.
        """
        try:
            connection = self._get_connection()
            cursor = connection.cursor()

            query = (
                f"INSERT INTO {self.TABLE_INVOICE} ({self.DEBT_ID}) VALUES (?)"
            )
            cursor.executemany(query, content)

            connection.commit()
            connection.close()
        except Exception as error:
            raise ErrorGenerator(6, f"Error inserting data: {error}")
