import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.simple_factory import UserFactory, UserType


def test_simple_factory():
    print("\n=== Testing Simple Factory Pattern ===")
    
    student = UserFactory.create_user(UserType.STUDENT, "U001", "student@university.edu", "John Doe")
    assert student.get_user_id() == "U001"
    assert student.get_email() == "student@university.edu"
    print(f"✓ Student created: {student}")
    
    admin = UserFactory.create_user(UserType.ADMIN, "U002", "admin@university.edu", "Jane Smith")
    assert admin.get_user_id() == "U002"
    print(f"✓ Admin created: {admin}")
    
    print("✅ Simple Factory Pattern test passed!\n")


if __name__ == "__main__":
    test_simple_factory()