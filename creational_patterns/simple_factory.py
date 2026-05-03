"""
SIMPLE FACTORY PATTERN
Use case: Centralized object creation for different user types
"""

from enum import Enum
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.user import User, UserRole


class UserType(Enum):
    STUDENT = "student"
    ADMIN = "admin"
    OFFICER = "officer"
    FINANCE = "finance"
    DINING = "dining"


class UserFactory:
    @staticmethod
    def create_user(user_type: UserType, user_id: str, email: str, name: str) -> User:
        role_mapping = {
            UserType.STUDENT: UserRole.STUDENT,
            UserType.ADMIN: UserRole.ADMIN,
            UserType.OFFICER: UserRole.OFFICER,
            UserType.FINANCE: UserRole.FINANCE,
            UserType.DINING: UserRole.DINING
        }
        
        role = role_mapping.get(user_type, UserRole.STUDENT)
        return User(user_id, email, name, role)


if __name__ == "__main__":
    print("=== Simple Factory Pattern Demo ===")
    
    student = UserFactory.create_user(UserType.STUDENT, "U001", "john@university.edu", "John Doe")
    admin = UserFactory.create_user(UserType.ADMIN, "U002", "jane@university.edu", "Jane Smith")
    officer = UserFactory.create_user(UserType.OFFICER, "U003", "bob@university.edu", "Bob Wilson")
    
    print(f"Created: {student}")
    print(f"Created: {admin}")
    print(f"Created: {officer}")
    print("✅ Simple Factory Pattern works!\n")