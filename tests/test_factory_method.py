import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.factory_method import (
    EmailNotificationFactory,
    PushNotificationFactory,
    SMSNotificationFactory
)


def test_factory_method():
    print("\n=== Testing Factory Method Pattern ===")
    
    email_factory = EmailNotificationFactory()
    result = email_factory.send_alert("Test message", "admin@university.edu")
    assert result == True
    print("✓ Email notification sent")
    
    push_factory = PushNotificationFactory()
    result = push_factory.send_alert("Test message", "admin_phone")
    assert result == True
    print("✓ Push notification sent")
    
    sms_factory = SMSNotificationFactory()
    result = sms_factory.send_alert("Test message", "+1234567890")
    assert result == True
    print("✓ SMS notification sent")
    
    print("✅ Factory Method Pattern test passed!\n")


if __name__ == "__main__":
    test_factory_method()