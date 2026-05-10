"""
Reward Repository Interface
"""

from abc import ABC
from typing import List, Optional
from src.reward import Reward

from repositories.repository_interface import Repository


class RewardRepository(Repository[Reward, str], ABC):
    """
    Entity-specific repository for Reward.
    """
    
    def find_by_status(self, status: str) -> List[Reward]:
        """Find rewards by status (available, limited, out_of_stock)"""
        pass
    
    def find_available_rewards(self) -> List[Reward]:
        """Find all rewards that are available for redemption"""
        pass
    
    def update_inventory(self, reward_id: str, quantity: int) -> None:
        """Update reward inventory count"""
        pass