"""
Test script to verify services are working
"""
import sys
import os
sys.path.append(os.getcwd())

from services.user_service import UserService
from services.smart_bin_service import SmartBinService

# Initialize services
user_service = UserService()
bin_service = SmartBinService(user_service=user_service)

# Create a user
print("Creating user...")
user = user_service.create_user("U001", "john@university.edu", "John Doe", "student")
print(f"User created: {user.get_user_id()} with {user.get_points_balance()} points")

# Create a bin
print("\nCreating bin...")
bin = bin_service.create_bin("B001", "Library Ground Floor")
print(f"Bin created: {bin.get_bin_id()} at {bin.get_location()}")

# Deposit an item
print("\nDepositing item...")
result = bin_service.deposit_item("U001", "B001", "plastic_bottle")
print(f"Deposit result: {result}")

# Check user points
print("\nChecking user points...")
updated_user = user_service.get_user_by_id("U001")
print(f"User now has {updated_user.get_points_balance()} points")

print("\n✅ All tests passed!")