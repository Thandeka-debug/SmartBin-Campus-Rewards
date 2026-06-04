"""
RewardService - Handles business logic for Reward operations
"""
from typing import List, Optional
from src.reward import Reward
from repositories.reward_repository import RewardRepository
from repositories.inmemory.inmemory_reward_repository import InMemoryRewardRepository
from services.user_service import UserService


class RewardService:
    """Service layer for Reward business logic"""
    
    def __init__(self, reward_repository: RewardRepository = None, user_service: UserService = None):
        self._repository = reward_repository or InMemoryRewardRepository()
        self._user_service = user_service or UserService()
    
    def create_reward(self, reward_id: str, name: str, point_cost: int, inventory: int) -> Reward:
        """Create a new reward.

        Args:
            reward_id (str): Unique identifier for the reward.
            name (str): Display name of the reward.
            point_cost (int): Number of points required to redeem this reward.
            inventory (int): Initial inventory count.

        Returns:
            Reward: The newly created Reward object.

        Raises:
            ValueError: If point_cost is not positive or inventory is negative.
        """
        if point_cost <= 0:
            raise ValueError("Point cost must be positive")
        if inventory < 0:
            raise ValueError("Inventory cannot be negative")
        
        reward = Reward(reward_id, name, point_cost, inventory)
        self._repository.save(reward)
        return reward
    
    def get_reward_by_id(self, reward_id: str) -> Optional[Reward]:
        """Get reward by ID.

        Args:
            reward_id (str): Unique identifier of the reward.

        Returns:
            Reward: The Reward object if found.

        Raises:
            ValueError: If the reward is not found.
        """
        reward = self._repository.find_by_id(reward_id)
        if not reward:
            raise ValueError(f"Reward with ID {reward_id} not found")
        return reward
    
    def get_all_rewards(self) -> List[Reward]:
        """Get all rewards.

        Returns:
            List[Reward]: A list of all Reward objects.
        """
        return self._repository.find_all()
    
    def get_available_rewards(self) -> List[Reward]:
        """Get only available rewards (inventory > 0).

        Returns:
            List[Reward]: A list of Reward objects that are currently in stock.
        """
        return self._repository.find_available_rewards()
    
    def redeem_reward(self, user_id: str, reward_id: str) -> dict:
        """Redeem a reward for a user.

        Args:
            user_id (str): ID of the user redeeming the reward.
            reward_id (str): ID of the reward to redeem.

        Returns:
            dict: A dictionary containing voucher_id, qr_code, points_deducted, and remaining_points.

        Raises:
            ValueError: If the reward is out of stock or the user has insufficient points.
        """
        user = self._user_service.get_user_by_id(user_id)
        reward = self.get_reward_by_id(reward_id)
        
        if reward.get_inventory_count() <= 0:
            raise ValueError("Reward is out of stock")
        if user.get_points_balance() < reward.get_point_cost():
            raise ValueError(f"Insufficient points. Need {reward.get_point_cost()}, have {user.get_points_balance()}")
        
        voucher = reward.redeem(user)
        self._repository.save(reward)
        
        return {
            "voucher_id": voucher.get_voucher_id(),
            "qr_code": voucher.get_qr_code(),
            "points_deducted": reward.get_point_cost(),
            "remaining_points": user.get_points_balance()
        }
    
    def publish_reward(self, reward_id: str) -> Reward:
        """Publish a reward (make it available).

        Args:
            reward_id (str): Unique identifier of the reward.

        Returns:
            Reward: The published Reward object.

        Raises:
            ValueError: If the reward is not found.
        """
        reward = self.get_reward_by_id(reward_id)
        reward.publish()
        self._repository.save(reward)
        return reward
