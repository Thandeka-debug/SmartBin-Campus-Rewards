"""
Transaction Repository Interface
"""

from abc import ABC
from typing import List, Optional
from datetime import datetime
from src.transaction import Transaction, ItemType

from repositories.repository_interface import Repository


class TransactionRepository(Repository[Transaction, str], ABC):
    """
    Entity-specific repository for Transaction.
    """
    
    def find_by_user_id(self, user_id: str) -> List[Transaction]:
        """Find all transactions for a specific user"""
        pass
    
    def find_by_bin_id(self, bin_id: str) -> List[Transaction]:
        """Find all transactions for a specific bin"""
        pass
    
    def find_by_item_type(self, item_type: ItemType) -> List[Transaction]:
        """Find all transactions for a specific item type"""
        pass
    
    def find_by_date_range(self, start: datetime, end: datetime) -> List[Transaction]:
        """Find transactions within a date range"""
        pass
    
    def get_total_points_by_user(self, user_id: str) -> int:
        """Get total points earned by a user"""
        pass