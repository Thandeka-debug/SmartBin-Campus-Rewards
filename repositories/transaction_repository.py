from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from src.transaction import Transaction
from repositories.repository_interface import Repository

class TransactionRepository(Repository[Transaction, str], ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> List[Transaction]:
        pass
    
    @abstractmethod
    def find_by_bin_id(self, bin_id: str) -> List[Transaction]:
        pass
    
    @abstractmethod
    def find_by_date_range(self, start: datetime, end: datetime) -> List[Transaction]:
        pass