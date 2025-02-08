import pytest
from main import parse_transaction

@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("test", None),
        ("test2", None),
    ],
)
def test_parse_transaction(input, expected):
    output = parse_transaction(input)
    assert output == expected
