from enum import Enum

class TxnCategory(Enum):
    OtherCategory = ("Other", "other")
    DebitCategory = ("Debit", "debit")
    DirectDepositCategory = ("Direct Deposit", "direct_deposit")
    InterestPaymentCategory = ("Interest Payment", "interest_payment")
    PurchaseCategory = ("Purchase", "purchase")
    WithdrawlCategory = ("Withdrawl", "withdrawl")

    name: str
    type: str

    def __init__(self, name: str, type: str):
        self._value = (name, type)
        self.name = name
        self.type = type




CATEGORIES = frozenset({
    TxnCategory.OtherCategory, # Default
    TxnCategory.DebitCategory,
    TxnCategory.DirectDepositCategory,
    TxnCategory.PurchaseCategory,
    TxnCategory.WithdrawlCategory
})