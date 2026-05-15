from abc import ABC, abstractmethod
from typing import List
from src.reward import Reward
from repositories.repository_interface import Repository

class RewardRepository(Repository[Reward, str], ABC):
    @abstractmethod
    def find_available_rewards(self) -> List[Reward]:
        pass
    
    @abstractmethod
    def update_inventory(self, reward_id: str, quantity: int) -> None:
        pass