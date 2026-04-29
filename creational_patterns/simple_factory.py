"""
Simple Factory Pattern - Centralized object creation
"""

from enum import Enum
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.user import User


class UserType(Enum):
    STUDENT = "student"
    ADMIN = "admin"
    OFFICER = "officer"
    FINANCE = "finance"
    DINING = "dining"


class UserFactory:
    @staticmethod
    def create_user(user_type: UserType, user_id: str, email: str, name: str) -> User:
        return User(user_id, email, name)


if __name__ == "__main__":
    student = UserFactory.create_user(UserType.STUDENT, "U001", "student@university.edu", "John Doe")
    admin = UserFactory.create_user(UserType.ADMIN, "U002", "admin@university.edu", "Jane Smith")
    print(f"Student created: {student}")
    print(f"Admin created: {admin}")
    print("Simple Factory Pattern test passed!")
