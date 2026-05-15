"""
Unit tests for RewardService
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pytest
from services.reward_service import RewardService
from services.user_service import UserService


class TestRewardService:
    def setup_method(self):
        self.user_service = UserService()
        self.reward_service = RewardService(user_service=self.user_service)
        self.user_service.create_user("U001", "john@university.edu", "John Doe", "student")
        self.user_service.update_user_points("U001", 100)
    
    def test_create_reward_success(self):
        reward = self.reward_service.create_reward("R001", "Coffee Voucher", 50, 100)
        assert reward.get_reward_id() == "R001"
    
    def test_create_reward_invalid_cost(self):
        with pytest.raises(ValueError, match="Point cost must be positive"):
            self.reward_service.create_reward("R001", "Coffee Voucher", -10, 100)
    
    def test_redeem_reward_insufficient_points(self):
        self.user_service.update_user_points("U001", 30)
        self.reward_service.create_reward("R001", "Coffee Voucher", 50, 100)
        with pytest.raises(ValueError, match="Insufficient points"):
            self.reward_service.redeem_reward("U001", "R001")