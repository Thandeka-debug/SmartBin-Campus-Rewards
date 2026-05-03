from enum import Enum
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.user import User
    from src.voucher import Voucher


class RewardStatus(Enum):
    DRAFT = "draft"
    AVAILABLE = "available"
    LIMITED = "limited"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"


class Reward:
    def __init__(self, reward_id: str, name: str, point_cost: int, inventory_count: int):
        self._reward_id = reward_id
        self._name = name
        self._description = ""
        self._point_cost = point_cost
        self._image_url = ""
        self._inventory_count = inventory_count
        self._status = RewardStatus.DRAFT
        self._created_at = datetime.now()

    def get_reward_id(self) -> str:
        return self._reward_id

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_point_cost(self) -> int:
        return self._point_cost

    def get_inventory_count(self) -> int:
        return self._inventory_count

    def get_status(self) -> RewardStatus:
        return self._status

    def set_description(self, description: str) -> 'Reward':
        self._description = description
        return self

    def set_image_url(self, url: str) -> 'Reward':
        self._image_url = url
        return self

    def publish(self) -> None:
        if self._status == RewardStatus.DRAFT:
            self._status = RewardStatus.AVAILABLE

    def redeem(self, user: 'User') -> 'Voucher':
        if self._inventory_count <= 0:
            raise Exception("Reward out of stock")
        if user.get_points_balance() < self._point_cost:
            raise Exception("Insufficient points")
        
        from src.voucher import Voucher
        voucher = Voucher.generate_voucher(user.get_user_id(), self._reward_id)
        user.update_points(-self._point_cost)
        self._inventory_count -= 1
        
        if self._inventory_count == 0:
            self._status = RewardStatus.OUT_OF_STOCK
        elif self._inventory_count < 5:
            self._status = RewardStatus.LIMITED
        
        return voucher

    def restock(self, quantity: int) -> None:
        self._inventory_count += quantity
        if self._status in [RewardStatus.OUT_OF_STOCK, RewardStatus.LIMITED]:
            self._status = RewardStatus.AVAILABLE

    def discontinue(self) -> None:
        self._status = RewardStatus.DISCONTINUED

    def __str__(self) -> str:
        return f"Reward(id={self._reward_id}, name={self._name}, cost={self._point_cost}, stock={self._inventory_count}, status={self._status.value})"