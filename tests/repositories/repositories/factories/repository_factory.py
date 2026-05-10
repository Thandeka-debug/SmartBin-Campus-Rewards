"""
Repository Factory - Creates the appropriate repository based on storage type.
This implements the Factory Pattern for storage abstraction.
"""

from typing import Any
from repositories.user_repository import UserRepository
from repositories.transaction_repository import TransactionRepository
from repositories.reward_repository import RewardRepository
from repositories.voucher_repository import VoucherRepository
from repositories.smart_bin_repository import SmartBinRepository
from repositories.alert_repository import AlertRepository
from repositories.report_repository import ReportRepository

# In-memory implementations
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from repositories.inmemory.inmemory_transaction_repository import InMemoryTransactionRepository
from repositories.inmemory.inmemory_reward_repository import InMemoryRewardRepository
from repositories.inmemory.inmemory_voucher_repository import InMemoryVoucherRepository
from repositories.inmemory.inmemory_smart_bin_repository import InMemorySmartBinRepository
from repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from repositories.inmemory.inmemory_report_repository import InMemoryReportRepository


class RepositoryFactory:
    """
    Factory for creating repository instances based on storage type.
    
    Supported storage types:
    - "memory": In-memory storage (HashMap)
    - "database": Database storage (stub for future)
    - "filesystem": Filesystem storage (stub for future)
    """
    
    @staticmethod
    def get_user_repository(storage_type: str = "memory") -> UserRepository:
        """Get User repository for the specified storage type"""
        if storage_type == "memory":
            return InMemoryUserRepository()
        elif storage_type == "database":
            # Future implementation: return DatabaseUserRepository()
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            # Future implementation: return FileSystemUserRepository()
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def get_transaction_repository(storage_type: str = "memory") -> TransactionRepository:
        """Get Transaction repository for the specified storage type"""
        if storage_type == "memory":
            return InMemoryTransactionRepository()
        elif storage_type == "database":
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def get_reward_repository(storage_type: str = "memory") -> RewardRepository:
        """Get Reward repository for the specified storage type"""
        if storage_type == "memory":
            return InMemoryRewardRepository()
        elif storage_type == "database":
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def get_voucher_repository(storage_type: str = "memory") -> VoucherRepository:
        """Get Voucher repository for the specified storage type"""
        if storage_type == "memory":
            return InMemoryVoucherRepository()
        elif storage_type == "database":
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def get_smart_bin_repository(storage_type: str = "memory") -> SmartBinRepository:
        """Get SmartBin repository for the specified storage type"""
        if storage_type == "memory":
            return InMemorySmartBinRepository()
        elif storage_type == "database":
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def get_alert_repository(storage_type: str = "memory") -> AlertRepository:
        """Get Alert repository for the specified storage type"""
        if storage_type == "memory":
            return InMemoryAlertRepository()
        elif storage_type == "database":
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def get_report_repository(storage_type: str = "memory") -> ReportRepository:
        """Get Report repository for the specified storage type"""
        if storage_type == "memory":
            return InMemoryReportRepository()
        elif storage_type == "database":
            raise NotImplementedError("Database storage not implemented yet")
        elif storage_type == "filesystem":
            raise NotImplementedError("Filesystem storage not implemented yet")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")