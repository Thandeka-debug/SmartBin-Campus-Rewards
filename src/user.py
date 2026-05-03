from enum import Enum
from datetime import datetime
from typing import Optional


class UserRole(Enum):
    STUDENT = "student"
    ADMIN = "admin"
    OFFICER = "officer"
    FINANCE = "finance"
    DINING = "dining"


class UserStatus(Enum):
    REGISTERED = "registered"
    VERIFIED = "verified"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DEACTIVATED = "deactivated"


class User:
    def __init__(self, user_id: str, email: str, name: str, role: UserRole = UserRole.STUDENT):
        self._user_id = user_id
        self._email = email
        self._name = name
        self._role = role
        self._password_hash = None
        self._points_balance = 0
        self._lifetime_points = 0
        self._status = UserStatus.REGISTERED
        self._created_at = datetime.now()
        self._last_login_at = None
        self._failed_attempts = 0

    def get_user_id(self) -> str:
        return self._user_id

    def get_email(self) -> str:
        return self._email

    def get_name(self) -> str:
        return self._name

    def get_role(self) -> UserRole:
        return self._role

    def get_points_balance(self) -> int:
        return self._points_balance

    def get_lifetime_points(self) -> int:
        return self._lifetime_points

    def get_status(self) -> UserStatus:
        return self._status

    def register(self, email: str, name: str, password: str) -> bool:
        if not email.endswith("@university.edu"):
            raise ValueError("Email must be a valid university email")
        self._email = email
        self._name = name
        self._password_hash = hash(password)
        self._status = UserStatus.REGISTERED
        return True

    def verify_email(self, token: str) -> bool:
        if token and self._status == UserStatus.REGISTERED:
            self._status = UserStatus.VERIFIED
            return True
        return False

    def login(self, email: str, password: str) -> Optional[str]:
        if self._status == UserStatus.SUSPENDED:
            raise Exception("Account is suspended")
        if self._email == email and self._password_hash == hash(password):
            self._status = UserStatus.ACTIVE
            self._last_login_at = datetime.now()
            self._failed_attempts = 0
            return f"session_token_{self._user_id}"
        else:
            self._failed_attempts += 1
            if self._failed_attempts >= 5:
                self._status = UserStatus.SUSPENDED
                raise Exception("Account suspended due to too many failed attempts")
            raise Exception("Invalid credentials")

    def update_points(self, points: int) -> None:
        self._points_balance += points
        if points > 0:
            self._lifetime_points += points

    def suspend(self) -> None:
        self._status = UserStatus.SUSPENDED

    def __str__(self) -> str:
        return f"User(id={self._user_id}, name={self._name}, points={self._points_balance}, status={self._status.value})"