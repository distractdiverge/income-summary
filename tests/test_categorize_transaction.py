import pytest
import datetime
from transaction_category import CATEGORIES, TxnCategory
from income_summarizer import categorize_transaction

@pytest.mark.parametrize(
        ("txn_description", "category"),
        [
            ("Interest Payment", TxnCategory.InterestPaymentCategory),
            ("Other Fin Inst ATM Surcharge Reimb", TxnCategory.OtherCategory),
            ("5661 Debit Card Purchase Pp*Apple.Com/Bill", TxnCategory.DebitCategory),
            ("POS Purchase Mirage Tobacco Horsham PA", TxnCategory.PurchaseCategory),
            ("5661 Recurring Debit Card Paypal *Hulu", TxnCategory.DebitCategory),
            ("Direct Deposit - ACH Trnsfr Mspbna", TxnCategory.DirectDepositCategory),
            ("Direct Deposit - Direct Dep", TxnCategory.DirectDepositCategory),
            ("ATM Withdrawal 1305 Main St Warrington PA", TxnCategory.WithdrawlCategory),
            ("Web Pmt- Inst Xfer Paypal Paramntplus", TxnCategory.PurchaseCategory),
            ("Direct Payment - Tesla Fina", TxnCategory.PurchaseCategory)
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
