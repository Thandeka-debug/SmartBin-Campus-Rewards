"""
UserService - Handles business logic for User operations
"""
from typing import List, Optional
from src.user import User, UserRole
from repositories.user_repository import UserRepository
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository


class UserService:
    """Service layer for User business logic"""
    
    def __init__(self, repository: UserRepository = None):
        self._repository = repository or InMemoryUserRepository()
    
    def create_user(self, user_id: str, email: str, name: str, role: str = "student") -> User:
        """Create a new user"""
        if self._repository.exists_by_id(user_id):
            raise ValueError(f"User with ID {user_id} already exists")
        if not email.endswith("@university.edu"):
            raise ValueError("Email must be a valid university email")
        
        role_map = {
            "student": UserRole.STUDENT,
            "admin": UserRole.ADMIN,
            "officer": UserRole.OFFICER,
            "finance": UserRole.FINANCE,
            "dining": UserRole.DINING
        }
        user_role = role_map.get(role.lower(), UserRole.STUDENT)
        user = User(user_id, email, name, user_role)
        self._repository.save(user)
        return user
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        user = self._repository.find_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return user
    
    def get_all_users(self) -> List[User]:
        """Get all users"""
        return self._repository.find_all()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        user = self._repository.find_by_email(email)
        if not user:
            raise ValueError(f"User with email {email} not found")
        return user
    
    def update_user_points(self, user_id: str, points: int) -> User:
        """Update user's points balance"""
        user = self.get_user_by_id(user_id)
        user.update_points(points)
        self._repository.save(user)
        return user
    
    def delete_user(self, user_id: str) -> None:
        """Delete a user"""
        if not self._repository.exists_by_id(user_id):
            raise ValueError(f"User with ID {user_id} not found")
        self._repository.delete(user_id)
    
    def get_users_by_role(self, role: str) -> List[User]:
        """Get users by role"""
        return self._repository.find_by_role(role)