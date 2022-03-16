from LineReader import readFromFile
import pytest
from unittest.mock import MagicMock


def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    # Replace the file.readline within the mock file to return "test line"
    mock_file.readline = MagicMock(return_value="test line")
    # Replace the file.open to return our mock file object rather than the actual file
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open) # Attach

    # Call the method under test
    result = readFromFile("blah")
    # Assert that it was called once with the given params
    mock_open.assert_called_once_with("blah",'r')
    # Assert that the correct string was returned
    assert result == "test line"