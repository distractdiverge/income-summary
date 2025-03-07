import pytest
from datetime import datetime
from main import parse_transaction
from transaction import Transaction

@pytest.mark.parametrize(
    ("input", "expected"),
    [
        # TODO: Replace 'expected' values to match new parsing of data
        (
            "01/17 30.00 XXXX Debit Card Purchase Paypal *Add To Bal", 
            Transaction(
                date=datetime(datetime.now().year, 1, 17), 
                amount=float(30.00), 
                description="XXXX Debit Card Purchase Paypal *Add To Bal"
            )
        ),
        (
            "08/29 .99 XXXX Debit Card Purchase Pp*Apple.Com/Bill", 
            Transaction(
                date=datetime(datetime.now().year, 8, 29), 
                amount=float(.99), 
                description="XXXX Debit Card Purchase Pp*Apple.Com/Bill"
            )
        ),
        ("test2", None),
        ("01/12 6,815.43 01/20 8,016.72 01/27 9,668.98 02/03 7,498.76", None)
    ],
)
def test_parse_transaction(input, expected):

    statement_from_date = datetime.now() # TODO: Replace with parameter (or test this feature separately)
    statement_to_date = statement_from_date

    actual = parse_transaction(input, statement_from_date, statement_to_date)

    if expected is None:
        assert actual is None
    else:
        assert actual is not None
                
        assert actual.date == expected.date
        assert actual.amount == expected.amount
        assert actual.description == expected.description
