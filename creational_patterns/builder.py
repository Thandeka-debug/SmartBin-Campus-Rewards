"""
BUILDER PATTERN
Use case: Construct complex Reward objects step-by-step
"""

from datetime import datetime


class Reward:
    def __init__(self, reward_id: str):
        self.reward_id = reward_id
        self.name = ""
        self.description = ""
        self.point_cost = 0
        self.image_url = ""
        self.inventory_count = 0
        self.tags = []
        self.categories = []
        self.created_at = datetime.now()
    
    def __str__(self) -> str:
        return (f"Reward(id={self.reward_id}, name='{self.name}', cost={self.point_cost}, "
                f"inventory={self.inventory_count})")


class RewardBuilder:
    def __init__(self, reward_id: str):
        self._reward = Reward(reward_id)
    
    def set_name(self, name: str) -> 'RewardBuilder':
        self._reward.name = name
        return self
    
    def set_description(self, description: str) -> 'RewardBuilder':
        self._reward.description = description
        return self
    
    def set_point_cost(self, cost: int) -> 'RewardBuilder':
        self._reward.point_cost = cost
        return self
    
    def set_image_url(self, url: str) -> 'RewardBuilder':
        self._reward.image_url = url
        return self
    
    def set_inventory(self, count: int) -> 'RewardBuilder':
        self._reward.inventory_count = count
        return self
    
    def add_tag(self, tag: str) -> 'RewardBuilder':
        self._reward.tags.append(tag)
        return self
    
    def add_category(self, category: str) -> 'RewardBuilder':
        self._reward.categories.append(category)
        return self
    
    def build(self) -> Reward:
        return self._reward


class RewardDirector:
    @staticmethod
    def create_coffee_voucher() -> Reward:
        return (RewardBuilder("R001")
                .set_name("Coffee Voucher")
                .set_description("Free coffee at campus cafe")
                .set_point_cost(50)
                .set_inventory(100)
                .add_category("Food")
                .add_tag("popular")
                .build())
    
    @staticmethod
    def create_merchandise() -> Reward:
        return (RewardBuilder("R002")
                .set_name("University T-Shirt")
                .set_description("Official university merchandise")
                .set_point_cost(200)
                .set_inventory(50)
                .add_category("Merchandise")
                .add_tag("limited")
                .build())


if __name__ == "__main__":
    print("=== Builder Pattern Demo ===")
    
    reward = (RewardBuilder("R003")
              .set_name("Water Bottle")
              .set_description("Reusable water bottle")
              .set_point_cost(75)
              .set_inventory(200)
              .add_tag("eco-friendly")
              .add_category("Merchandise")
              .build())
    
    print(f"Built reward: {reward}")
    
    coffee = RewardDirector.create_coffee_voucher()
    print(f"Coffee Voucher: {coffee}")
    
    tshirt = RewardDirector.create_merchandise()
    print(f"T-Shirt: {tshirt}")
    
    print("\n✅ Builder Pattern works!")