"""
Voucher Repository Interface
"""

from abc import ABC
from typing import List, Optional
from src.voucher import Voucher

from repositories.repository_interface import Repository


class VoucherRepository(Repository[Voucher, str], ABC):
    """
    Entity-specific repository for Voucher.
    """
    
    def find_by_user_id(self, user_id: str) -> List[Voucher]:
        """Find all vouchers for a specific user"""
        pass
    
    def find_by_status(self, status: str) -> List[Voucher]:
        """Find vouchers by status (generated, redeemed, expired)"""
        pass
    
    def find_valid_vouchers(self) -> List[Voucher]:
        """Find all vouchers that are not expired or redeemed"""
        pass