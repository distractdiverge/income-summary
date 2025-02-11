from datetime import datetime
from typing import NamedTuple
from transaction_category import TxnCategory

class Transaction(NamedTuple):
    date: datetime
    amount: float
    category: TxnCategory
    description: str
