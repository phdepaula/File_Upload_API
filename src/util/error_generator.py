class ErrorGenerator(Exception):
    """
    Class to gerenate a specific error.
    """

    def __init__(self, error_code: int, message: str):
        self.error_code = error_code
        self.message = message
        super().__init__(message)

    def get_error_description(self) -> str:
        """
        Method to get error description
        """
        description = (
            "Error generated.\n"
            + f"Error Code: {self.error_code}.\n"
            + f"Message: {self.message}."
        )

        return description
