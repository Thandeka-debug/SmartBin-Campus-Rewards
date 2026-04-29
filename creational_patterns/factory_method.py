"""
Factory Method Pattern - Delegate instantiation to subclasses
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> bool:
        pass


class EmailNotification(Notification):
    def send(self, message: str, recipient: str) -> bool:
        print(f"Sending EMAIL to {recipient}: {message}")
        return True


class PushNotification(Notification):
    def send(self, message: str, recipient: str) -> bool:
        print(f"Sending PUSH notification to {recipient}: {message}")
        return True


class SMSNotification(Notification):
    def send(self, message: str, recipient: str) -> bool:
        print(f"Sending SMS to {recipient}: {message}")
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
    factories = [EmailNotificationFactory(), PushNotificationFactory(), SMSNotificationFactory()]
    
    for factory in factories:
        result = factory.send_alert("Bin is 90% full!", "admin@university.edu")
        print(f"Result: {result}")
    
    print("Factory Method Pattern test passed!")
