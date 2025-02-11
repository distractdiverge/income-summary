from enum import Enum

class TxnCategory(Enum):
    name: str
    type: str

    def __init__(self, name: str, type: str):
        self._value = (name, type)
        self.name = name
        self.type = type

CATEGORIES = frozenset({
    TxnCategory("Other", "other"), # Default
    TxnCategory("Debit", "debit"),
    TxnCategory("Purchase", "purchase"),
    TxnCategory("Withdrawl", "withdrawl")
})