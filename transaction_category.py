from enum import Enum

class TxnCategory(Enum):
    OtherCategory = ("Other", "other")
    DebitCategory = ("Debit", "debit")
    DirectDepositCategory = ("Direct Deposit", "direct_deposit")
    InterestPaymentCategory = ("Interest Payment", "interest_payment")
    IncomeCategory = ("Income", "income")
    PurchaseCategory = ("Purchase", "purchase")
    WithdrawlCategory = ("Withdrawl", "withdrawl")

    type: str

    def __init__(self, name: str, type: str):
        self._value = (name, type)
        self.type = type

CATEGORIES = frozenset({
    TxnCategory.OtherCategory, # Default
    TxnCategory.DebitCategory,
    TxnCategory.DirectDepositCategory,
    TxnCategory.InterestPaymentCategory,
    TxnCategory.IncomeCategory,
    TxnCategory.PurchaseCategory,
    TxnCategory.WithdrawlCategory
})