'''
Abstract Factory Pattern for Notifications
Problem Statement
You are working on a notification system for a communication application. The application must support different types of notifications,
such as email, SMS, and push notifications. Each notification type has specific content and delivery methods. You want to design a flexible
notification system where different types of notifications can be created without specifying their concrete classes, ensuring the system is open for
future notification types and supports compatibility within families.

Assignment
Your task is to implement the Abstract Factory pattern to create notifications and related components in the communication application. The Abstract
Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes, allowing for easy
addition of new notification types and ensuring compatibility within families.

Task 1 - Defining the Abstract Factory
The abstract factory class has been created for you. You will need to add the factory methods to create the notification, templates, and senders to the
abstract factory class. The method notificationType has already been abstracted out for you as an example. You will need to implement the
NotificationFactory class as a common parent class for all the notification factories.

Task 2 - Implementing Concrete Factories
Create concrete implementations of the NotificationFactory interface for email and push notifications. Implement the methods to create compatible
notifications, notification providers, and notification templates for each notification type. Ensure that the created components are compatible within
the same family.

Task 3 - Testing the Implementation
Run the provided test cases in the NotificationFactoryTest class to verify the correctness of your implementation. The tests will check if all
notifications have a common parent class, and if the factory classes can correctly create notifications, notification providers, and notification
templates based on the notification type and content.

Instructions
Implement the NotificationFactory interface with methods to create notifications, notification providers, and notification templates.

Create concrete implementations of the NotificationFactory interface for email, SMS, and push notifications. Implement the methods to create compatible
components for each notification type.

Run the provided test cases in the NotificationFactoryTest class to verify the correctness of your implementation. The tests will ensure that the factory
classes can correctly create notification components based on the notification type and content.
'''