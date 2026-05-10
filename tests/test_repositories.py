"""
Unit tests for In-Memory Repositories (CRUD operations)
"""

import sys
import os
import uuid
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from datetime import datetime
from src.user import User, UserRole
from src.transaction import Transaction, ItemType
from src.reward import Reward
from src.voucher import Voucher
from src.smart_bin import SmartBin
from src.alert import Alert, AlertSeverity
from src.report import Report, ReportType

from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from repositories.inmemory.inmemory_transaction_repository import InMemoryTransactionRepository
from repositories.inmemory.inmemory_reward_repository import InMemoryRewardRepository
from repositories.inmemory.inmemory_voucher_repository import InMemoryVoucherRepository
from repositories.inmemory.inmemory_smart_bin_repository import InMemorySmartBinRepository
from repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from repositories.inmemory.inmemory_report_repository import InMemoryReportRepository

from factories.repository_factory import RepositoryFactory


class TestUserRepository:
    """Test CRUD operations for UserRepository"""
    
    def setup_method(self):
        """Setup before each test"""
        self.repo = InMemoryUserRepository()
        self.test_user = User("U001", "test@university.edu", "Test User", UserRole.STUDENT)
    
    def test_save_and_find_by_id(self):
        """Test Create and Read operations"""
        self.repo.save(self.test_user)
        found = self.repo.find_by_id("U001")
        assert found is not None
        assert found.get_user_id() == "U001"
        assert found.get_name() == "Test User"
    
    def test_find_all(self):
        """Test Read All operation"""
        self.repo.save(self.test_user)
        user2 = User("U002", "test2@university.edu", "Test User 2", UserRole.ADMIN)
        self.repo.save(user2)
        
        all_users = self.repo.find_all()
        assert len(all_users) == 2
    
    def test_delete(self):
        """Test Delete operation"""
        self.repo.save(self.test_user)
        assert self.repo.exists_by_id("U001") == True
        
        self.repo.delete("U001")
        assert self.repo.exists_by_id("U001") == False
    
    def test_find_by_email(self):
        """Test entity-specific find_by_email"""
        self.repo.save(self.test_user)
        found = self.repo.find_by_email("test@university.edu")
        assert found is not None
        assert found.get_user_id() == "U001"
    
    def test_find_by_role(self):
        """Test entity-specific find_by_role"""
        self.repo.save(self.test_user)
        admin = User("U002", "admin@university.edu", "Admin User", UserRole.ADMIN)
        self.repo.save(admin)
        
        students = self.repo.find_by_role("student")
        assert len(students) == 1
        assert students[0].get_role().value == "student"
    
    def test_update_points(self):
        """Test entity-specific update_points"""
        self.repo.save(self.test_user)
        self.repo.update_points("U001", 50)
        
        updated = self.repo.find_by_id("U001")
        assert updated.get_points_balance() == 50


class TestTransactionRepository:
    """Test CRUD operations for TransactionRepository"""
    
    def setup_method(self):
        self.repo = InMemoryTransactionRepository()
        self.test_transaction = Transaction.create_transaction(
            "U001", "B001", ItemType.PLASTIC_BOTTLE
        )
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.test_transaction)
        found = self.repo.find_by_id(self.test_transaction.get_transaction_id())
        assert found is not None
        assert found.get_user_id() == "U001"
    
    def test_find_all(self):
        self.repo.save(self.test_transaction)
        trans2 = Transaction.create_transaction("U002", "B001", ItemType.ALUMINUM_CAN)
        self.repo.save(trans2)
        
        all_trans = self.repo.find_all()
        assert len(all_trans) == 2
    
    def test_delete(self):
        self.repo.save(self.test_transaction)
        trans_id = self.test_transaction.get_transaction_id()
        assert self.repo.exists_by_id(trans_id) == True
        
        self.repo.delete(trans_id)
        assert self.repo.exists_by_id(trans_id) == False
    
    def test_find_by_user_id(self):
        self.repo.save(self.test_transaction)
        transactions = self.repo.find_by_user_id("U001")
        assert len(transactions) == 1
    
    def test_get_total_points_by_user(self):
        self.repo.save(self.test_transaction)
        # Points are 10 for plastic bottle (from POINTS_MAP)
        # We need to award points first
        from src.user import User
        user = User("U001", "test@university.edu", "Test User")
        self.test_transaction.award_points(user)
        self.repo.save(self.test_transaction)
        
        total = self.repo.get_total_points_by_user("U001")
        assert total == 10


class TestRewardRepository:
    """Test CRUD operations for RewardRepository"""
    
    def setup_method(self):
        self.repo = InMemoryRewardRepository()
        self.test_reward = Reward("R001", "Coffee Voucher", 50, 100)
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.test_reward)
        found = self.repo.find_by_id("R001")
        assert found is not None
        assert found.get_name() == "Coffee Voucher"
    
    def test_find_available_rewards(self):
        self.repo.save(self.test_reward)
        self.test_reward.publish()
        self.repo.save(self.test_reward)
        
        available = self.repo.find_available_rewards()
        assert len(available) == 1


class TestRepositoryFactory:
    """Test Factory Pattern for storage abstraction"""
    
    def test_create_memory_user_repository(self):
        repo = RepositoryFactory.get_user_repository("memory")
        assert isinstance(repo, InMemoryUserRepository)
    
    def test_create_invalid_storage_type(self):
        import pytest
        with pytest.raises(ValueError):
            RepositoryFactory.get_user_repository("invalid")
    
    def test_factory_returns_independent_instances(self):
        repo1 = RepositoryFactory.get_user_repository("memory")
        repo2 = RepositoryFactory.get_user_repository("memory")
        
        # They should be different instances but same type
        assert repo1 is not repo2
        assert isinstance(repo1, InMemoryUserRepository)
        assert isinstance(repo2, InMemoryUserRepository)


def test_factory_pattern_demo():
    """Demonstrate how Factory Pattern enables storage switching"""
    print("\n=== Repository Factory Pattern Demo ===")
    
    # Create repositories using Factory
    user_repo = RepositoryFactory.get_user_repository("memory")
    transaction_repo = RepositoryFactory.get_transaction_repository("memory")
    
    # Save a user
    user = User("U001", "demo@university.edu", "Demo User")
    user_repo.save(user)
    print(f"✓ Saved user: {user.get_name()}")
    
    # Retrieve the user
    found = user_repo.find_by_id("U001")
    print(f"✓ Retrieved user: {found}")
    
    # Demonstrate future storage switching (would work by changing "memory" to "database")
    print("\n✓ Factory pattern enables easy storage switching.")
    print("  To use database storage, change 'memory' to 'database' in factory call.")
    print("  Then implement DatabaseXxxRepository classes.")


if __name__ == "__main__":
    # Run tests
    test_user_repo = TestUserRepository()
    test_user_repo.setup_method()
    test_user_repo.test_save_and_find_by_id()
    test_user_repo.test_find_all()
    test_user_repo.test_delete()
    test_user_repo.test_find_by_email()
    test_user_repo.test_find_by_role()
    test_user_repo.test_update_points()
    print("✅ All UserRepository tests passed!")
    
    test_trans_repo = TestTransactionRepository()
    test_trans_repo.setup_method()
    test_trans_repo.test_save_and_find_by_id()
    test_trans_repo.test_find_all()
    test_trans_repo.test_delete()
    test_trans_repo.test_find_by_user_id()
    print("✅ All TransactionRepository tests passed!")
    
    test_reward_repo = TestRewardRepository()
    test_reward_repo.setup_method()
    test_reward_repo.test_save_and_find_by_id()
    test_reward_repo.test_find_available_rewards()
    print("✅ All RewardRepository tests passed!")
    
    test_factory = TestRepositoryFactory()
    test_factory.test_create_memory_user_repository()
    test_factory.test_create_invalid_storage_type()
    test_factory.test_factory_returns_independent_instances()
    print("✅ All Factory Pattern tests passed!")
    
    test_factory_pattern_demo()
    
    print("\n" + "="*50)
    print("ALL REPOSITORY TESTS PASSED! ✅")
    print("="*50)