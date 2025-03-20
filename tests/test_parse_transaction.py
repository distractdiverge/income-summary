import pytest
from datetime import datetime
from main import parse_transaction
from transaction import Transaction

@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            "02/15 45.00 1234 Debit Card Purchase Example *Coffee Shop", 
            Transaction(
                date=datetime(datetime.now().year, 2, 15), 
                amount=float(45.00), 
                description="1234 Debit Card Purchase Example *Coffee Shop"
            )
        ),
        (
            "07/10 .99 5678 Debit Card Purchase Example *Online Store", 
            Transaction(
                date=datetime(datetime.now().year, 7, 10), 
                amount=float(.99), 
                description="5678 Debit Card Purchase Example *Online Store"
            )
        ),
        (
            "01/10 .99 5678 Debit Card Purchase Example January", 
            Transaction(
                date=datetime(datetime.now().year, 1, 10), 
                amount=float(.99), 
                description="5678 Debit Card Purchase Example January"
            )
        ),
        ("invalid_data", None),
        ("03/22 1,234.56 03/29 2,345.67 04/05 3,456.78 04/12 4,567.89", None)
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
