import pytest
from main import parse_transaction

@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("01/17 30.00 XXXX Debit Card Purchase Paypal *Add To Bal", 
            ("01/17", "30.00", "XXXX Debit Card Purchase Paypal *Add To Bal")),
        ("test2", None),
    ],
)
def test_parse_transaction(input, expected):
    actual = parse_transaction(input)

    if expected is None:
        assert actual is None
    else:
        date, amount, description = actual
        
        expected_date, expected_amount, expected_description = expected
        assert date == expected_date
        assert amount == expected_amount
        assert description == expected_description
