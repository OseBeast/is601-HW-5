"main.py test"
import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, operation_string, b_string, expected_string", [
    ("5", '+', "3",  "5 + 3 = 8.0"),
    ("10", '-', "2",  "10 - 2 = 8.0"),
    ("4", '*', "5",  "4 * 5 = 20.0"),
    ("20", '/', "4",  "20 / 4 = 5.0"),
    ("1", '/', "0",  "1 / 0 = Error: Cannot divide by zero"),
    ("9", "unknown", "3", "Unknown operation: unknown"),
    ("a", '+', "3", "Invalid number input: a or 3"),
    ("5", '-', "b", "Invalid number input: 5 or b")
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    "functional test"
    calculate_and_print(a_string, operation_string, b_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
