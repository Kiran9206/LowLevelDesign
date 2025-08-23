'''
Simple Factory Pattern for Notification System
Problem Statement
You are designing a notification system. Depending on the type of notification (e.g., email, SMS, push notification), different notification
routines are required. You need a way to create notifications without explicitly specifying their classes, ensuring the system is open for future
notification types.

Assignment
Your task is to implement the Simple Factory pattern to create notifications in the notification system. The Simple Factory pattern provides a way to
create objects without exposing the instantiation logic, allowing for easy addition of new notification types.

Task 1 - Creating a Common Parent Class - Product Hierarchy
Complete the common product class Notification: Start by completing the parent AudioPlayer class. This is going to be the parent class for each
supported notification format. Each notification class should implement the same set of methods sending notifications. Additionally, each class
should have attributes that store information about the notification, such as the recipient and message. Make sure to use the same names of the
methods and attributes in the parent class. Also, abstract common methods with the same implementation in the parent class.

Modify the concrete product classes (e.g., EmailNotification, SMSNotification, PushNotification): Implement the concrete notification classes for
each supported notification format. Each class should inherit from the Notification class and implement the methods to send notifications.

Task 2 - Implementing the Simple Factory
Next, complete the NotificationFactory class that follows the Simple Factory pattern. This class should provide a static method create_notification
to create notification objects based on the notification type and relevant arguments. The factory class should take care of instantiating the
appropriate notification class based on the type provided and the relevant arguments. Remember you have to create the actual concrete notification
objects in the factory class so pass the required arguments to the factory method. Looking to the args parameter in the create_notification method,
you can use *args to pass a variable number of arguments to the method.

Instructions
Implement the Notification class as a common parent class for all notfications. Include attributes and methods that are common to all notifications.

Implement the NotificationFactory class that implements the Simple Factory pattern. Add a method create_notification to create notification objects
based on the notification type and relevant arguments (recipient, sender, message).

Run the provided test cases in the NotificationTest class to verify the correctness of your implementation. The tests will check if all notification
classes are implemented correctly and if the factory class is able to create notification objects for different notification types.
'''


from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipient, message, sender=None):
        self.recipient = recipient
        self.message = message
        self.sender = sender

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return f"Sending Email to {self.recipient}: {self.message}"

class SMSNotification(Notification):
    def send(self):
        return f"Sending SMS to {self.recipient}: {self.message}"

class PushNotification(Notification):
    def send(self):
        return f"Sending Push Notification to {self.recipient}: {self.message}"


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type, *args):
        if notification_type == "email":
            return EmailNotification(*args)
        elif notification_type == "sms":
            return SMSNotification(*args)
        elif notification_type == "push":
            return PushNotification(*args)
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

class NotificationTest:

    @staticmethod
    def run_tests():

        sender =  "kiran@gamil.com"
        recipient = "kumar@gmail.com"
        message = "Hello, this is a test notification."
        # Test Email Notification
        email_notification = NotificationFactory.create_notification('email', recipient, message, sender)
        assert isinstance(email_notification, EmailNotification), "Email notification creation failed"
        assert email_notification.send() == f"Sending Email to {recipient}: {message}", "Email notification send failed"
        print(email_notification.send())
        # Test SMS Notification
        sms_notification = NotificationFactory.create_notification('sms', recipient, message)
        assert isinstance(sms_notification, SMSNotification), "SMS notification creation failed"
        assert sms_notification.send() == f"Sending SMS to {recipient}: {message}", "SMS notification send failed"
        print(sms_notification.send())
        # Test Push Notification
        push_notification = NotificationFactory.create_notification('push', recipient, message)
        assert isinstance(push_notification, PushNotification), "Push notification creation failed"
        assert push_notification.send() == f"Sending Push Notification to {recipient}: {message}", "Push notification send failed"
        print(push_notification.send())
        # Test Unknown Notification Type
        try:
            unknown_notification = NotificationFactory.create_notification('fax', recipient, message)
        except ValueError as e:
            assert str(e) == "Unknown notification type: fax", "Unknown notification type handling failed"
            print(e)

if __name__ == "__main__":
    NotificationTest.run_tests()
