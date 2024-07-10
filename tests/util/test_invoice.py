from datetime import datetime

from src.util.error_generator import ErrorGenerator
from src.util.invoice import Invoice


def test_invoice_generation():
    """
    Method to test if invoice is being generated.
    """
    name = "  John Doe  "
    government_id = "11111111111"
    email = "johndoe@kanastra.com.br"
    debt_amount = "1000000.00"
    debt_due_date = "2024-01-19"
    debt_id = "1adb6ccf-ff16-467f-bea7-5f05d494280f"

    invoice = Invoice(
        name, government_id, email, debt_amount, debt_due_date, debt_id
    )

    assert invoice.name == "John Doe"
    assert isinstance(invoice.government_id, int)
    assert isinstance(invoice.debt_amount, float)
    assert invoice.debt_amount == 1000000.00
    assert isinstance(invoice.debt_due_date, datetime)


def test_invoice_generation_with_wrong_date():
    """
    Method to test if invoice is being generated.
    """
    name = "  John Doe  "
    government_id = "11111111111"
    email = "johndoe@kanastra.com.br"
    debt_amount = "1000000.00"
    debt_due_date = "2024-19-01"
    debt_id = "1adb6ccf-ff16-467f-bea7-5f05d494280f"

    error_code = ""

    try:
        invoice = Invoice(
            name, government_id, email, debt_amount, debt_due_date, debt_id
        )
    except ErrorGenerator as error:
        error_code = error.error_code

    assert error_code == 4
