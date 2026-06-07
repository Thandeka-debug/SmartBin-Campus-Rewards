"""
UserService - Handles business logic for User operations
"""
from typing import List, Optional
from src.user import User, UserRole
from repositories.user_repository import UserRepository
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository


class UserService:
    """
    Service layer for User business logic.
    
    This service handles all user-related operations including creation,
    retrieval, updates, and deletion. It acts as an intermediary between
    the API layer and the repository layer.
    
    Attributes:
        _repository (UserRepository): Repository instance for user data persistence.
    """
    
    def __init__(self, repository: UserRepository = None):
        """
        Initialize UserService with an optional repository.
        
        Args:
            repository (UserRepository, optional): Custom repository implementation.
                Defaults to InMemoryUserRepository if not provided.
        """
        self._repository = repository or InMemoryUserRepository()
    
    def create_user(self, user_id: str, email: str, name: str, role: str = "student") -> User:
        """
        Create a new user.
        
        Args:
            user_id (str): Unique identifier for the user.
            email (str): User's email address (must end with @university.edu).
            name (str): User's full name.
            role (str, optional): User role. Defaults to "student".
                Valid values: student, admin, officer, finance, dining.
        
        Returns:
            User: The newly created User object.
        
        Raises:
            ValueError: If user ID already exists or email is not a university email.
        """
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
        """
        Get user by ID.
        
        Args:
            user_id (str): Unique identifier of the user to retrieve.
        
        Returns:
            Optional[User]: User object if found.
        
        Raises:
            ValueError: If user with the given ID does not exist.
        """
        user = self._repository.find_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return user
    
    def get_all_users(self) -> List[User]:
        """
        Get all users.
        
        Returns:
            List[User]: List of all User objects in the system.
        """
        return self._repository.find_all()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Get user by email.
        
        Args:
            email (str): Email address of the user to retrieve.
        
        Returns:
            Optional[User]: User object if found.
        
        Raises:
            ValueError: If user with the given email does not exist.
        """
        user = self._repository.find_by_email(email)
        if not user:
            raise ValueError(f"User with email {email} not found")
        return user
    
    def update_user_points(self, user_id: str, points: int) -> User:
        """
        Update user's points balance.
        
        Args:
            user_id (str): Unique identifier of the user.
            points (int): New points balance to set.
        
        Returns:
            User: Updated User object.
        """
        user = self.get_user_by_id(user_id)
        user.update_points(points)
        self._repository.save(user)
        return user
    
    def delete_user(self, user_id: str) -> None:
        """
        Delete a user.
        
        Args:
            user_id (str): Unique identifier of the user to delete.
        
        Raises:
            ValueError: If user with the given ID does not exist.
        """
        if not self._repository.exists_by_id(user_id):
            raise ValueError(f"User with ID {user_id} not found")
        self._repository.delete(user_id)
    
    def get_users_by_role(self, role: str) -> List[User]:
        """
        Get users by role.
        
        Args:
            role (str): Role name to filter by (student, admin, officer, finance, dining).
        
        Returns:
            List[User]: List of User objects with the specified role.
        """
        return self._repository.find_by_role(role)