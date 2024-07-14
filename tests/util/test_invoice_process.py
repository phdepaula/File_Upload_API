from datetime import datetime
from unittest.mock import patch

from src.database.invoice_database import Invoice_Database
from src.util.invoice_process import InvoiceProcess
from src.util.log_generator import LogGenerator


@patch.object(InvoiceProcess, "_save_new_invoices_in_database")
@patch.object(LogGenerator, "_close_log")
@patch.object(LogGenerator, "_add_new_log")
@patch.object(LogGenerator, "_create_log_file")
@patch.object(Invoice_Database, "get_all_data")
def test_invoice_process(
    mock_get_all_data,
    mock_create_log_file,
    mock_add_new_log,
    mock_close_log,
    mock_save_new_invoices_in_database,
):
    """
    Method responsible for teste invoice process
    """
    mock_get_all_data.return_value = []
    mock_create_log_file.return_value = None
    mock_add_new_log.return_value = None
    mock_close_log.return_value = None
    mock_save_new_invoices_in_database.return_value = None

    invoice_process = InvoiceProcess()
    invoice_process.execute_invoice_process()

    start_date = invoice_process.start_date
    end_date = invoice_process.end_date
    invoices_added = invoice_process.invoices_added
    email_sent = invoice_process.email_sent

    quantity_of_invoices = len(invoices_added)
    quantity_of_email = len(email_sent)

    assert isinstance(start_date, datetime)
    assert isinstance(end_date, datetime)
    assert quantity_of_invoices == 1100000
    assert quantity_of_email == 1100000
