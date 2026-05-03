import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.builder import RewardBuilder, RewardDirector


def test_builder():
    print("\n=== Testing Builder Pattern ===")
    
    reward = (RewardBuilder("R001")
              .set_name("Test Reward")
              .set_description("This is a test reward")
              .set_point_cost(100)
              .set_inventory(50)
              .add_tag("test")
              .add_category("Test Category")
              .build())
    
    assert reward.name == "Test Reward"
    assert reward.point_cost == 100
    assert reward.inventory_count == 50
    print(f"✓ Reward built successfully: {reward}")
    
    coffee = RewardDirector.create_coffee_voucher()
    assert coffee.name == "Coffee Voucher"
    assert coffee.point_cost == 50
    print(f"✓ Coffee voucher created: {coffee}")
    
    print("✅ Builder Pattern test passed!\n")


if __name__ == "__main__":
    test_builder()