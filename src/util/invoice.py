from datetime import datetime

from src.util.error_generator import ErrorGenerator


class Invoice:
    """
    Class to generate a invoice
    """

    def __init__(
        self,
        name: str,
        government_id: str,
        email: str,
        debt_amount: str,
        debt_due_date: str,
        debt_id: str,
    ) -> None:
        self.name = name
        self.government_id = government_id
        self.email = email
        self.debt_amount = debt_amount
        self.debt_due_date = debt_due_date
        self.debt_id = debt_id

        self._fix_attributes()

    def _convert_to_float(self, text: str) -> int:
        """
        Method reponsible for converting a text to float.
        """
        return float(text)

    def _convert_to_integer(self, text: str) -> int:
        """
        Method reponsible for converting a text to integer.
        """
        return int(text)

    def _convert_to_datetime(self, date: str) -> datetime:
        """
        Method responsible for converting a date in str
        in datetime.
        """
        divided_date = date.split("-")
        year = self._convert_to_integer(divided_date[0])
        month = self._convert_to_integer(divided_date[1])
        day = self._convert_to_integer(divided_date[2])

        return datetime(year, month, day)

    def _fix_attributes(self) -> None:
        """
        Method responsible for fixing atributtes types
        """
        try:
            self.name = self._remove_extra_spaces(self.name)
            self.government_id = self._convert_to_integer(self.government_id)
            self.email = self._remove_extra_spaces(self.email)
            self.debt_amount = self._convert_to_float(self.debt_amount)
            self.debt_due_date = self._convert_to_datetime(self.debt_due_date)
            self.debt_id = self._remove_extra_spaces(self.debt_id)
        except Exception as error:
            raise ErrorGenerator(
                4, f"Error fixing invoice attributes: {error}"
            )

    def _remove_extra_spaces(self, text: str) -> str:
        """
        Method to remove extra spaces at the beginning
        and end of the string
        """
        return text.strip()

    def create_invoice(self) -> str:
        """
        Method responsible for creating invoice.
        """
        try:
            message = f"Creating invoice: {self.debt_id}"
            return message
        except Exception as error:
            raise ErrorGenerator(8, f"Error creating invoice: {error}")
