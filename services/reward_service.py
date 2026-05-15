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
        """Create a new reward"""
        if point_cost <= 0:
            raise ValueError("Point cost must be positive")
        if inventory < 0:
            raise ValueError("Inventory cannot be negative")
        
        reward = Reward(reward_id, name, point_cost, inventory)
        self._repository.save(reward)
        return reward
    
    def get_reward_by_id(self, reward_id: str) -> Optional[Reward]:
        """Get reward by ID"""
        reward = self._repository.find_by_id(reward_id)
        if not reward:
            raise ValueError(f"Reward with ID {reward_id} not found")
        return reward
    
    def get_all_rewards(self) -> List[Reward]:
        """Get all rewards"""
        return self._repository.find_all()
    
    def get_available_rewards(self) -> List[Reward]:
        """Get only available rewards"""
        return self._repository.find_available_rewards()
    
    def redeem_reward(self, user_id: str, reward_id: str) -> dict:
        """Redeem a reward for a user"""
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
        """Publish a reward (make it available)"""
        reward = self.get_reward_by_id(reward_id)
        reward.publish()
        self._repository.save(reward)
        return reward