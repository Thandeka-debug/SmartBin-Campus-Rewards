"""
In-Memory implementation of RewardRepository
"""

from typing import Dict, List, Optional
from src.reward import Reward, RewardStatus

from repositories.reward_repository import RewardRepository


class InMemoryRewardRepository(RewardRepository):
    """
    Stores Reward objects in a Python dictionary (HashMap).
    """
    
    def __init__(self):
        self._storage: Dict[str, Reward] = {}
    
    def save(self, entity: Reward) -> None:
        """Save or update a reward"""
        self._storage[entity.get_reward_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[Reward]:
        """Find a reward by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[Reward]:
        """Get all rewards"""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete a reward by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists_by_id(self, id: str) -> bool:
        """Check if a reward exists"""
        return id in self._storage
    
    def find_by_status(self, status: str) -> List[Reward]:
        """Find rewards by status"""
        return [r for r in self._storage.values() if r.get_status().value == status]
    
    def find_available_rewards(self) -> List[Reward]:
        """Find all rewards that are available for redemption"""
        return [r for r in self._storage.values() 
                if r.get_status() in [RewardStatus.AVAILABLE, RewardStatus.LIMITED]]
    
    def update_inventory(self, reward_id: str, quantity: int) -> None:
        """Update reward inventory count"""
        reward = self.find_by_id(reward_id)
        if reward:
            if quantity > reward.get_inventory_count():
                reward.restock(quantity - reward.get_inventory_count())
            else:
                # In a real implementation, you would have a decrement method
                pass