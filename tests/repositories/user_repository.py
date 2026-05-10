"""
User Repository Interface
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from src.user import User

from repositories.repository_interface import Repository


class UserRepository(Repository[User, str], ABC):
    """
    Entity-specific repository for User.
    Extends generic Repository with User-specific methods.
    """
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Find a user by their email address"""
        pass
    
    @abstractmethod
    def find_by_role(self, role: str) -> List[User]:
        """Find all users with a specific role"""
        pass
    
    @abstractmethod
    def update_points(self, user_id: str, points: int) -> None:
        """Update a user's points balance"""
        pass