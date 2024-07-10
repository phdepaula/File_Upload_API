from src.util.email_sender import EmailSender


def test_email_sender():
    """
    Method to teste email sender.
    """
    email = "johndoe@kanastra.com.br"
    message = "Test Message"

    email_sender = EmailSender(email, message)
    feedback = email_sender.execute_email_sender()

    assert feedback == (f"Email sent {email}.\n" + f"Message: {message}.")
