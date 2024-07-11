from typing import List

from src.util.invoice import Invoice


class InvoiceProcess:
    """
    Class to execute invoice Process
    """

    def __init__(self) -> None:
        self.invoices_added = []

    def _create_invoice(self, data: List) -> None:
        """
        Method responsible for creating invoice.
        """
        invoice = Invoice(*data)
        invoice.create_invoice()

    def _add_invoice(self, data: List) -> None:
        """
        Method to insert the invoice into table.
        """
        debt_id = data[5]
        self.invoices_added.append(debt_id)

    def execute_process_invoice(self, data: List) -> None:
        """
        Method responsible for executin
        """
        self._create_invoice(data)
        self._add_invoice(data)
