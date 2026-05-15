"""
Unit tests for UserService
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pytest
from services.user_service import UserService


class TestUserService:
    def setup_method(self):
        self.service = UserService()
    
    def test_create_user_success(self):
        user = self.service.create_user("U001", "john@university.edu", "John Doe", "student")
        assert user.get_user_id() == "U001"
    
    def test_create_user_invalid_email(self):
        with pytest.raises(ValueError, match="Email must be a valid university email"):
            self.service.create_user("U002", "john@gmail.com", "John Doe", "student")
    
    def test_get_user_by_id_not_found(self):
        with pytest.raises(ValueError, match="User with ID U999 not found"):
            self.service.get_user_by_id("U999")