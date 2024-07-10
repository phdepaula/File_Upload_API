class EmailSender:
    """
    Method responsible for sendind Email.
    """

    SUCCESS = "Success"
    ERROR = "Error"

    def __init__(self, email: str, message: str):
        self.email = email
        self.message = message

    def execute_email_sender(self) -> str:
        """
        Method responsible for executing email sender.
        """
        try:
            self._send_email()
            return self._get_feedback(self.SUCCESS)
        except Exception as error:
            return self._get_feedback(self.ERROR, error)

    def _get_feedback(self, status: str, error_message: str = "") -> str:
        """
        Method to get feedback of
        the sent email.
        """
        feedback = (
            (f"Email sent {self.email}.\n" + f"Message: {self.message}.")
            if status == self.SUCCESS
            else (f"Error sending the e-mail.\n" + f"Error: {error_message}.")
        )

        return feedback

    def _send_email(self) -> None:
        """
        Method responsible for sending an email
        """
        print(f"Sending email to {self.email}.")
