from abc import ABC, abstractmethod
from typing import List
from src.voucher import Voucher
from repositories.repository_interface import Repository

class VoucherRepository(Repository[Voucher, str], ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> List[Voucher]:
        pass