"""
In-Memory implementation of TransactionRepository
"""

from typing import Dict, List, Optional
from datetime import datetime
from src.transaction import Transaction, ItemType

from repositories.transaction_repository import TransactionRepository


class InMemoryTransactionRepository(TransactionRepository):
    """
    Stores Transaction objects in a Python dictionary (HashMap).
    """
    
    def __init__(self):
        self._storage: Dict[str, Transaction] = {}
    
    def save(self, entity: Transaction) -> None:
        """Save or update a transaction"""
        self._storage[entity.get_transaction_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[Transaction]:
        """Find a transaction by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[Transaction]:
        """Get all transactions"""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete a transaction by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists_by_id(self, id: str) -> bool:
        """Check if a transaction exists"""
        return id in self._storage
    
    def find_by_user_id(self, user_id: str) -> List[Transaction]:
        """Find all transactions for a specific user"""
        return [t for t in self._storage.values() if t.get_user_id() == user_id]
    
    def find_by_bin_id(self, bin_id: str) -> List[Transaction]:
        """Find all transactions for a specific bin"""
        return [t for t in self._storage.values() if t.get_bin_id() == bin_id]
    
    def find_by_item_type(self, item_type: ItemType) -> List[Transaction]:
        """Find all transactions for a specific item type"""
        return [t for t in self._storage.values() if t.get_item_type() == item_type]
    
    def find_by_date_range(self, start: datetime, end: datetime) -> List[Transaction]:
        """Find transactions within a date range"""
        return [t for t in self._storage.values() if start <= t._timestamp <= end]
    
    def get_total_points_by_user(self, user_id: str) -> int:
        """Get total points earned by a user"""
        return sum(t.get_points_earned() for t in self.find_by_user_id(user_id))