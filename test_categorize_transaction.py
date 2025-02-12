import pytest
import datetime
from transaction_category import CATEGORIES, TxnCategory
from main import categorize_transaction

@pytest.mark.parametrize(
        ("txn_description", "category"),
        [
            ("Direct Deposit - ACH Trnsfr Mspbna", TxnCategory.DirectDepositCategory),
            ("Interest Payment", TxnCategory.InterestPaymentCategory),
            ("Other Fin Inst ATM Surcharge Reimb", TxnCategory.OtherCategory),
            ("5661 Debit Card Purchase Pp*Apple.Com/Bill", TxnCategory.DebitCategory),
            ("POS Purchase Mirage Tobacco Horsham PA", TxnCategory.PurchaseCategory),
            ("5661 Recurring Debit Card Paypal *Hulu", TxnCategory.DebitCategory)
        ]
)
def test_categorize_transaction(txn_description, category):
    print(f"Description: {repr(txn_description)}")
    print(f"Category: {repr(category)}")

    output = categorize_transaction(txn_description)
    assert output is not None
    assert category is not None

    assert output in CATEGORIES
    assert output.type == category.type
