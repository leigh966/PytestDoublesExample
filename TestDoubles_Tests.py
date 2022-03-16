from LineReader import readFromFile
from pytest import *
from unittest.mock import MagicMock


def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    # Replace the file.readline within the mock file to return "test line"
    mock_file.readline = MagicMock(return_value="test line")
    # Replace the file.open to return our mock file object rather than the actual file
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open) # Attach
    # os.path.exists will return true
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    # Call the method under test
    result = readFromFile("blah")
    # Assert that it was called once with the given params
    mock_open.assert_called_once_with("blah",'r')
    # Assert that the correct string was returned
    assert result == "test line"

def test_throwsExcetionWithBadFile(monkeypatch):
    mock_file = MagicMock()
    # Replace the file.readline within the mock file to return "test line"
    mock_file.readline = MagicMock(return_value="test line")
    # Replace the file.open to return our mock file object rather than the actual file
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open) # Attach
    # os.path.exists will return false
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        # Call the method under test
        result = readFromFile("blah")