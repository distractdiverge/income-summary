from datetime import datetime
from typing import NamedTuple


class TxnCategory(NamedTuple):
    name: str
    type: str

CATEGORIES = frozenset({
    TxnCategory("Other", "other"), # Default
    TxnCategory("Debit", "debit"),
    TxnCategory("Purchase", "purchase"),
    TxnCategory("Withdrawl", "withdrawl")
})

class Transaction(NamedTuple):
    date: datetime
    amount: float
    category: TxnCategory
    description: str
