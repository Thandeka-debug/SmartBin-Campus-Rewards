"""
Unit tests for SmartBinService
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pytest
from services.smart_bin_service import SmartBinService
from services.user_service import UserService


class TestSmartBinService:
    def setup_method(self):
        self.user_service = UserService()
        self.bin_service = SmartBinService(user_service=self.user_service)
        self.user_service.create_user("U001", "john@university.edu", "John Doe", "student")
        self.user_service.update_user_points("U001", 100)
        self.bin_service.create_bin("B001", "Library")
    
    def test_create_bin_success(self):
        bin = self.bin_service.create_bin("B002", "Cafeteria")
        assert bin.get_bin_id() == "B002"
    
    def test_update_fill_level(self):
        bin = self.bin_service.update_bin_fill_level("B001", 50)
        assert bin.get_fill_level() == 50
    
    def test_deposit_item_success(self):
        result = self.bin_service.deposit_item("U001", "B001", "plastic_bottle")
        assert result["points_earned"] == 10