from abc import ABC, abstractmethod
from typing import Optional, List
from src.user import User
from repositories.repository_interface import Repository

class UserRepository(Repository[User, str], ABC):
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_by_role(self, role: str) -> List[User]:
        pass
    
    @abstractmethod
    def update_points(self, user_id: str, points: int) -> None:
        pass