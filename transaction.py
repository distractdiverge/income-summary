from datetime import datetime
from typing import NamedTuple, Optional
from transaction_category import TxnCategory

class Transaction(NamedTuple):
    date: datetime
    amount: float
    description: str
    category: Optional[TxnCategory] = None
