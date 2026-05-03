"""
FACTORY METHOD PATTERN
Use case: Different notification services for alerts
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> bool:
        pass


class EmailNotification(Notification):
    def send(self, message: str, recipient: str) -> bool:
        print(f"  Sending EMAIL to {recipient}: {message}")
        return True


class PushNotification(Notification):
    def send(self, message: str, recipient: str) -> bool:
        print(f"  Sending PUSH notification to {recipient}: {message}")
        return True


class SMSNotification(Notification):
    def send(self, message: str, recipient: str) -> bool:
        print(f"  Sending SMS to {recipient}: {message}")
        return True


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
    
    def send_alert(self, message: str, recipient: str) -> bool:
        notification = self.create_notification()
        return notification.send(message, recipient)


class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()


class PushNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()


class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()


if __name__ == "__main__":
    print("=== Factory Method Pattern Demo ===")
    
    factories = [
        ("Email", EmailNotificationFactory()),
        ("Push", PushNotificationFactory()),
        ("SMS", SMSNotificationFactory())
    ]
    
    for name, factory in factories:
        print(f"\nTesting {name} notification:")
        result = factory.send_alert("Bin is 90% full!", "admin@university.edu")
        print(f"  Result: {'Success' if result else 'Failed'}")
    
    print("\n✅ Factory Method Pattern works!")