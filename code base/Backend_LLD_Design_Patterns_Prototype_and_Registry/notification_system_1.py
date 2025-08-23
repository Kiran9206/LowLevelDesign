'''
Abstract Factory Pattern for Notifications
Problem Statement
You are working on a notification system for a communication application. The application must support different types of notifications,
such as email, SMS, and push notifications. Each notification type has specific content and delivery methods. You want to design a flexible
notification system where different types of notifications can be created without specifying their concrete classes, ensuring the system is
open for future notification types and supports compatibility within families.

Assignment
Your task is to implement the Abstract Factory pattern to create notifications and related components in the communication application. The Abstract
Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes, allowing for
easy addition of new notification types and ensuring compatibility within families.

Task 1 - Adding the factory methods to the abstract factory
The abstract factory class NotificationFactory has been created for you. You will need to add the factory methods to create notification,
templates and senders to the abstract factory class. The methods to be implemented are:

create_notification
create_template
create_sender
Task 2 - Implementing the Abstract Factory
Now that you have the abstract factory class, you will need to implement the abstract factory for different types of notifications such as
EmailNotification, and PushNotification. Two classes have been created for you: EmailNotificationFactory and PushNotificationFactory.
You will need to implement the methods to create compatible notifications, templates, and senders. Ensure that the created components are compatible
within the same format family.

Instructions
Complete the NotificationFactory interface with methods to create notifications, templates, and senders. Methods to be implemented are:
create_notification
create_template
create_sender
Complete the concrete implementations of the NotificationFactory interface for email and push notification formats. Implement the methods to create
compatible notifications, templates, and senders. The classes to be implemented are:
EmailNotificationFactory
PushNotificationFactory
Run the provided test cases in the TestNotificationFactory class to verify the correctness of your implementation. The tests will check if all
notification components have a common parent class, and if the factory classes can correctly create notifications, templates, and senders based
on the notification type.
'''

from abc import ABC, abstractmethod



class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass
    @abstractmethod
    def create_template(self):
        pass
    @abstractmethod
    def create_sender(self):
        pass

# creating the interfaces for Notification, Template and Sender

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class Template(ABC):
    @abstractmethod
    def format(self, message):
        pass

class Sender(ABC):
    @abstractmethod
    def send(self, formatted_message):
        pass

# Implementing Email Notification components

class EmailNotification(Notification):
    def notify(self, message):
        return f"Email Notification: {message}"

class EmailTemplate(Template):
    def format(self, message):
        return f"Email Template: {message}"

class EmailSender(Sender):
    def send(self, formatted_message):
        return f"Sending Email: {formatted_message}"

# Implementing Push Notification components

class PushNotification(Notification):
    def notify(self, message):
        return f"Push Notification: {message}"

class PushTemplate(Template):
    def format(self, message):
        return f"Push Template: {message}"

class PushSender(Sender):
    def send(self, formatted_message):
        return f"Sending Push Notification: {formatted_message}"

# Email Factory Implementation

class EmailNotificationFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()

    def create_template(self):
        return EmailTemplate()

    def create_sender(self):
        return EmailSender()

# Push Notification Factory Implementation
class PushNotificationFactory(NotificationFactory):
    def create_notification(self):
        return PushNotification()

    def create_template(self):
        return PushTemplate()

    def create_sender(self):
        return PushSender()

class TestNotificationFactory:

    @staticmethod
    def test_notification( factory: NotificationFactory, message: str):
        notification = factory.create_notification()
        template = factory.create_template()
        sender = factory.create_sender()

        formatted_message = template.format(message)
        notification_message = notification.notify(formatted_message)
        send_status = sender.send(notification_message)

        return send_status

if __name__ == "__main__":
    email_factory = EmailNotificationFactory()
    push_factory = PushNotificationFactory()

    email_result = TestNotificationFactory.test_notification(email_factory, "Hello via Email!")
    push_result = TestNotificationFactory.test_notification(push_factory, "Hello via Push Notification!")

    print(email_result)  # Output: Sending Email: Email Notification: Email Template: Hello via Email!
    print(push_result)   # Output: Sending Push Notification: Push Notification: Push Template: Hello via Push Notification!

