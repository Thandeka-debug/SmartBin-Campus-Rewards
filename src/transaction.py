from enum import Enum
from datetime import datetime
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from src.user import User


class ItemType(Enum):
    PLASTIC_BOTTLE = "plastic_bottle"
    ALUMINUM_CAN = "aluminum_can"
    GLASS_BOTTLE = "glass_bottle"
    PAPER = "paper"


class TransactionStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class Transaction:
    POINTS_MAP = {
        ItemType.PLASTIC_BOTTLE: 10,
        ItemType.ALUMINUM_CAN: 8,
        ItemType.GLASS_BOTTLE: 12,
        ItemType.PAPER: 5
    }

    def __init__(self, transaction_id: str, user_id: str, bin_id: str, item_type: ItemType):
        self._transaction_id = transaction_id
        self._user_id = user_id
        self._bin_id = bin_id
        self._item_type = item_type
        self._points_earned = 0
        self._timestamp = datetime.now()
        self._status = TransactionStatus.PENDING

    def get_transaction_id(self) -> str:
        return self._transaction_id

    def get_user_id(self) -> str:
        return self._user_id

    def get_bin_id(self) -> str:
        return self._bin_id

    def get_item_type(self) -> ItemType:
        return self._item_type

    def get_points_earned(self) -> int:
        return self._points_earned

    def get_status(self) -> TransactionStatus:
        return self._status

    @classmethod
    def create_transaction(cls, user_id: str, bin_id: str, item_type: ItemType) -> 'Transaction':
        transaction_id = str(uuid.uuid4())
        return cls(transaction_id, user_id, bin_id, item_type)

    @classmethod
    def calculate_points(cls, item_type: ItemType) -> int:
        return cls.POINTS_MAP.get(item_type, 0)

    def award_points(self, user: 'User') -> bool:
        if self._status != TransactionStatus.PENDING:
            return False
        self._status = TransactionStatus.PROCESSING
        self._points_earned = self.calculate_points(self._item_type)
        user.update_points(self._points_earned)
        self._status = TransactionStatus.COMPLETED
        return True

    def fail_transaction(self, reason: str) -> None:
        self._status = TransactionStatus.FAILED
        print(f"Transaction failed: {reason}")

    def __str__(self) -> str:
        return f"Transaction(id={self._transaction_id}, points={self._points_earned}, status={self._status.value})"