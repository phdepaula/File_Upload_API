from src.util.error_generator import ErrorGenerator


def test_generating_error():
    """
    Teste to check if the error is generated.
    """
    error = ErrorGenerator(1, "Error Test")
    description = error.get_error_description()

    result = "Error generated.\nError Code: 1.\nMessage: Error Test."

    assert description == result
