import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.prototype import BinCache


def test_prototype():
    print("\n=== Testing Prototype Pattern ===")
    
    BinCache.load_cache()
    
    bin1 = BinCache.get_bin("standard")
    bin1.bin_id = "B003"
    bin1.location = "Library Ground Floor"
    
    bin2 = BinCache.get_bin("standard")
    bin2.bin_id = "B004"
    bin2.location = "Cafeteria"
    
    assert bin1 is not bin2
    assert bin1.bin_id != bin2.bin_id
    print(f"✓ Bin 1: {bin1}")
    print(f"✓ Bin 2: {bin2}")
    
    high_traffic = BinCache.get_bin("high_traffic")
    assert high_traffic.configuration["warning_threshold"] == 70
    print(f"✓ High traffic bin cloned: {high_traffic}")
    
    print("✅ Prototype Pattern test passed!\n")


if __name__ == "__main__":
    test_prototype()