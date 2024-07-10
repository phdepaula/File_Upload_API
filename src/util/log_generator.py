import os
from datetime import datetime

from src.util.error_generator import ErrorGenerator


class LogGenerator:
    """
    Class to gererate log files.
    """

    def __init__(self, name: str):
        self.name = name
        self.log_path = None
        self._create_log_file()

    def _add_new_log(self, message: str) -> None:
        """
        Method to add message to the log.
        """
        try:
            with open(self.log_path, "a") as file:
                text = f"\n{self._get_current_time()} {message}"
                file.write(text)
        except Exception as error:
            raise ErrorGenerator(3, f"Error adding log: {error}")

    def _create_log_file(self) -> None:
        """
        Method to create log file
        """
        try:
            log_directory = os.path.join(os.getcwd(), "log")

            if not os.path.exists(log_directory):
                os.makedirs(log_directory)

            self.log_path = os.path.join(log_directory, f"{self.name}.log")

            with open(self.log_path, "w") as file:
                text = f"{self._get_current_time()} Log Started\n"
                file.write(text)
        except Exception as error:
            raise ErrorGenerator(2, f"Error creating log: {error}")

    def _get_current_time(self) -> str:
        """
        Method to get current time.
        """
        date = datetime.now()
        date_formated = date.strftime("%Y-%m-%d %H:%M:%S")

        return date_formated
