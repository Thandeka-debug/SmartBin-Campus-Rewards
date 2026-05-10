"""
In-Memory implementation of VoucherRepository
"""

from typing import Dict, List, Optional
from src.voucher import Voucher, VoucherStatus

from repositories.voucher_repository import VoucherRepository


class InMemoryVoucherRepository(VoucherRepository):
    """
    Stores Voucher objects in a Python dictionary (HashMap).
    """
    
    def __init__(self):
        self._storage: Dict[str, Voucher] = {}
    
    def save(self, entity: Voucher) -> None:
        """Save or update a voucher"""
        self._storage[entity.get_voucher_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[Voucher]:
        """Find a voucher by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[Voucher]:
        """Get all vouchers"""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete a voucher by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists_by_id(self, id: str) -> bool:
        """Check if a voucher exists"""
        return id in self._storage
    
    def find_by_user_id(self, user_id: str) -> List[Voucher]:
        """Find all vouchers for a specific user"""
        return [v for v in self._storage.values() if v.get_user_id() == user_id]
    
    def find_by_status(self, status: str) -> List[Voucher]:
        """Find vouchers by status"""
        return [v for v in self._storage.values() if v.get_status().value == status]
    
    def find_valid_vouchers(self) -> List[Voucher]:
        """Find all vouchers that are not expired or redeemed"""
        return [v for v in self._storage.values() 
                if v.get_status() not in [VoucherStatus.EXPIRED, VoucherStatus.REDEEMED, VoucherStatus.INVALID]]