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