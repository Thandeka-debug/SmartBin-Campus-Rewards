"""
In-Memory implementation of UserRepository
"""

from typing import Dict, Optional, List
from src.user import User

from repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    """
    Stores User objects in a Python dictionary (HashMap).
    """
    
    def __init__(self):
        self._storage: Dict[str, User] = {}
    
    def save(self, entity: User) -> None:
        """Save or update a user"""
        self._storage[entity.get_user_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[User]:
        """Find a user by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[User]:
        """Get all users"""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete a user by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists_by_id(self, id: str) -> bool:
        """Check if a user exists"""
        return id in self._storage
    
    def find_by_email(self, email: str) -> Optional[User]:
        """Find a user by email"""
        for user in self._storage.values():
            if user.get_email() == email:
                return user
        return None
    
    def find_by_role(self, role: str) -> List[User]:
        """Find all users with a specific role"""
        return [user for user in self._storage.values() if user.get_role().value == role]
    
    def update_points(self, user_id: str, points: int) -> None:
        """Update a user's points balance"""
        user = self.find_by_id(user_id)
        if user:
            user.update_points(points)
    
    def __len__(self) -> int:
        """Return number of users (helper for testing)"""
        return len(self._storage)