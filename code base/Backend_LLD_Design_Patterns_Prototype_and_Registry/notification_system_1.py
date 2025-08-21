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