"""
SmartBinService - Handles business logic for SmartBin operations
"""
from typing import List, Optional
from src.smart_bin import SmartBin
from repositories.smart_bin_repository import SmartBinRepository
from repositories.inmemory.inmemory_smart_bin_repository import InMemorySmartBinRepository
from services.user_service import UserService
from src.transaction import Transaction, ItemType


class SmartBinService:
    """Service layer for SmartBin business logic"""
    
    def __init__(self, bin_repository: SmartBinRepository = None, user_service: UserService = None):
        self._repository = bin_repository or InMemorySmartBinRepository()
        self._user_service = user_service or UserService()
        self._transactions = []
    
    def create_bin(self, bin_id: str, location: str) -> SmartBin:
        """Create a new smart bin.

        Args:
            bin_id (str): Unique identifier for the bin.
            location (str): Physical location of the bin.

        Returns:
            SmartBin: The newly created SmartBin object.

        Raises:
            ValueError: If a bin with the given ID already exists.
        """
        if self._repository.exists_by_id(bin_id):
            raise ValueError(f"Bin with ID {bin_id} already exists")
        bin = SmartBin(bin_id, location)
        self._repository.save(bin)
        return bin
    
    def get_bin_by_id(self, bin_id: str) -> Optional[SmartBin]:
        """Get bin by ID.

        Args:
            bin_id (str): Unique identifier of the bin.

        Returns:
            SmartBin: The SmartBin object if found.

        Raises:
            ValueError: If the bin is not found.
        """
        bin = self._repository.find_by_id(bin_id)
        if not bin:
            raise ValueError(f"Bin with ID {bin_id} not found")
        return bin
    
    def get_all_bins(self) -> List[SmartBin]:
        """Get all bins.

        Returns:
            List[SmartBin]: A list of all SmartBin objects.
        """
        return self._repository.find_all()
    
    def update_bin_fill_level(self, bin_id: str, fill_level: int) -> SmartBin:
        """Update bin fill level.

        Args:
            bin_id (str): Unique identifier of the bin.
            fill_level (int): New fill level (0-100).

        Returns:
            SmartBin: The updated SmartBin object.

        Raises:
            ValueError: If fill_level is not between 0 and 100.
        """
        if fill_level < 0 or fill_level > 100:
            raise ValueError("Fill level must be between 0 and 100")
        
        bin = self.get_bin_by_id(bin_id)
        bin.update_fill_level(fill_level)
        self._repository.save(bin)
        return bin
    
    def deposit_item(self, user_id: str, bin_id: str, item_type: str) -> dict:
        """Deposit an item into a bin.

        Args:
            user_id (str): ID of the user performing the deposit.
            bin_id (str): ID of the target bin.
            item_type (str): Type of the item (e.g., "plastic_bottle", "aluminum_can", "glass_bottle", "paper").

        Returns:
            dict: A dictionary containing transaction details such as transaction_id, points_earned, bin_fill_level, and a message.

        Raises:
            ValueError: If the bin is full or the item_type is invalid.
        """
        user = self._user_service.get_user_by_id(user_id)
        bin = self.get_bin_by_id(bin_id)
        
        if not bin.check_capacity():
            raise ValueError("Bin is full. Please use another bin.")
        
        item_type_map = {
            "plastic_bottle": ItemType.PLASTIC_BOTTLE,
            "aluminum_can": ItemType.ALUMINUM_CAN,
            "glass_bottle": ItemType.GLASS_BOTTLE,
            "paper": ItemType.PAPER
        }
        
        item_enum = item_type_map.get(item_type.lower())
        if not item_enum:
            raise ValueError(f"Invalid item type: {item_type}")
        
        transaction = Transaction.create_transaction(user_id, bin_id, item_enum)
        points_earned = transaction.calculate_points(item_enum)
        transaction.award_points(user)
        bin.add_deposit()
        self._repository.save(bin)
        self._transactions.append(transaction)
        
        return {
            "transaction_id": transaction.get_transaction_id(),
            "points_earned": points_earned,
            "bin_fill_level": bin.get_fill_level(),
            "message": f"Successfully deposited {item_type}. You earned {points_earned} points!"
        }
    
    def empty_bin(self, bin_id: str) -> SmartBin:
        """Empty a bin.

        Args:
            bin_id (str): Unique identifier of the bin.

        Returns:
            SmartBin: The emptied SmartBin object.

        Raises:
            ValueError: If the bin is not found.
        """
        bin = self.get_bin_by_id(bin_id)
        bin.empty_bin()
        self._repository.save(bin)
        return bin
    
    def get_bins_needing_emptying(self, threshold: int = 80) -> List[SmartBin]:
        """Get bins that need emptying based on fill level threshold.

        Args:
            threshold (int, optional): Fill level percentage above which bins are considered needing emptying. Defaults to 80.

        Returns:
            List[SmartBin]: A list of SmartBin objects with fill level >= threshold.
        """
        return self._repository.find_bins_needing_emptying(threshold)
