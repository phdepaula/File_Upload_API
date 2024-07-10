import os
from unittest.mock import patch

from src.util.log_generator import LogGenerator


@patch.object(LogGenerator, "_get_current_time")
def test_creating_log_file(mock_get_current_time):
    """
    Method to test the creation of a lof file.
    """
    mock_get_current_time.return_value = "2024-07-09 22:00:00"

    name = "test_file"
    log_generator = LogGenerator(name)
    log_generator._add_new_log("New Text")

    log_path = log_generator.log_path

    with open(log_path, "r") as file:
        content = file.read()

    os.remove(log_path)

    result = (
        "2024-07-09 22:00:00 Log Started\n" + "\n2024-07-09 22:00:00 New Text"
    )

    assert content == result
