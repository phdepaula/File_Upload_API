import concurrent.futures
import os
from datetime import datetime
from typing import Dict, List

from src.database.invoice_database import Invoice_Database
from src.util.email_sender import EmailSender
from src.util.error_generator import ErrorGenerator
from src.util.invoice import Invoice
from src.util.log_generator import LogGenerator
from src.util.pandas_handler import PandasHandler


class InvoiceProcess:
    """
    Class to execute invoice Process
    """

    # PATHS
    INPUT_PATH = os.path.join(os.getcwd(), "assets", "input.csv")

    # General Constants
    DEBT_ID_COLUMN = "debtId"
    DATE = "date"
    STRING = "string"

    def __init__(self) -> None:
        self.start_date = None
        self.end_date = None
        self.runtime = None
        self.invoices_added = []
        self.email_sent = []
        self.__pandas_handler = PandasHandler(self.INPUT_PATH)
        self.__invoice_database = Invoice_Database()
        self.__log = None

    def _create_invoice(self, data: List) -> Invoice:
        """
        Method responsible for creating invoice.
        """
        invoice = Invoice(*data)
        self.invoices_added.append(invoice.debt_id)

        return invoice

    def _filter_new_invoices_to_generate(self) -> List:
        """
        Method responsible for filtering invoices to be
        generated.
        """
        self.__log._add_new_log("Filtering invoices.")

        new_invoices = self._get_new_invoices()
        self.__pandas_handler.filter_dataframe(
            self.DEBT_ID_COLUMN, new_invoices
        )

    def _generate_new_invoices(self) -> None:
        """
        Method responsible for generating new invoices.
        """
        new_data = self.__pandas_handler.get_dataframe_values()

        quantity_of_data = len(new_data)

        if quantity_of_data > 0:
            self.__log._add_new_log(
                f"There are {quantity_of_data} invoices to be generated."
            )

            with concurrent.futures.ThreadPoolExecutor(
                max_workers=100
            ) as executor:
                executor.map(self._execute_invoice_generator_steps, new_data)

            invoices_text = ", ".join(self.invoices_added)
            self.__log._add_new_log(f"Invoices created: {invoices_text}")

            email_text = ", ".join(self.email_sent)
            self.__log._add_new_log(f"Email sent to: {email_text}")

            self._save_new_invoices_in_database()
        else:
            self.__log._add_new_log("There are no new invoices.")

    def _get_current_date(self) -> Dict:
        """
        Method responsible for getting current date.
        """
        date = datetime.now()
        date_string = date.strftime("%Y_%m_%d_%H_%M_%S")

        return {self.DATE: date, self.STRING: date_string}

    def _get_runtime(self) -> None:
        """
        Method responsible for getting run time
        """
        self.__log._close_log(self.start_date, self.end_date)
        self.runtime = self.__log.runtime

    def _get_new_invoices(self) -> List:
        """
        Method responsible for getting new invoices.
        """
        input_invoices = set(
            self.__pandas_handler.get_values_from_column_to_compare(
                self.DEBT_ID_COLUMN
            )
        )
        invoices_generated = set(self.__invoice_database.get_all_data())

        new_invoices = list(
            input_invoices.symmetric_difference(invoices_generated)
        )

        return new_invoices

    def _start_log(self) -> None:
        """
        Method responsible for staring log generator.
        """
        log_name = "invoice_process_" + self._get_current_date()[self.STRING]
        self.__log = LogGenerator(log_name)

    def _read_input_file(self) -> None:
        """
        Method responsible for reading input file.
        """
        separator = ","
        data_type = {
            "name": str,
            "governmentId": str,
            "email": str,
            "debtAmount": str,
            "debtDueDate": str,
            "debtId": str,
        }

        self.__log._add_new_log(f"Reading file: {self.INPUT_PATH}")
        self.__pandas_handler.read_csv(separator, data_type)

    def _execute_invoice_generator_steps(self, data: List) -> None:
        """
        Method responsible for executing all steps
        to generate a invoice.
        """
        invoice = self._create_invoice(data)
        self._send_email(invoice)

    def _save_new_invoices_in_database(self) -> None:
        """
        Method responsible for saving the new invoices generated to database.
        """
        self.__log._add_new_log("Saving new invoices to database.")
        self.__invoice_database.create_database_file(self.invoices_added)

    def _send_email(self, invoice: Invoice) -> None:
        """
        Method responsible for sending email.
        """
        email = invoice.email
        debt_id = invoice.debt_id
        message = f"Invoice generated with the following debt id {debt_id}"

        email_sender = EmailSender(email, message)
        email_sender.execute_email_sender()

        self.email_sent.append(email)

    def _set_start_date(self) -> None:
        """
        Method to set start date
        """
        self.start_date = self._get_current_date()[self.DATE]

    def _set_end_date(self) -> None:
        """
        Method to set start date
        """
        self.end_date = self._get_current_date()[self.DATE]

    def execute_invoice_process(self) -> None:
        """
        Method responsible for executing invoice process
        """
        try:
            self._set_start_date()
            self._start_log()
            self._read_input_file()
            self._filter_new_invoices_to_generate()
            self._generate_new_invoices()
            self._set_end_date()
            self._get_runtime()
        except ErrorGenerator as error:
            self.__log._add_new_log(f"Error: {error.get_error_description()}")
            raise error
        except Exception as error:
            self.__log._add_new_log(f"Error: {error}")
            raise ErrorGenerator(
                10, f"Error executing process invoice: {error}"
            )
