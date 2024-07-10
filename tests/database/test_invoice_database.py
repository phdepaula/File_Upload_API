import os

from src.database.invoice_database import Invoice_Database


def test_database_creation():
    """
    Method to test if database will be created.
    """
    invoice_database = Invoice_Database()
    database_path = invoice_database.database_path

    assert os.path.exists(database_path) is True