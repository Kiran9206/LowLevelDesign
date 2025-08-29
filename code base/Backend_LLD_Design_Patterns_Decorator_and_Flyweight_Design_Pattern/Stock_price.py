'''
Observer Pattern for Stock Trading Platform
Problem Statement
You are developing a stock trading platform where users need to be notified whenever the price of a particular stock crosses a certain threshold. These notifications should be sent through various channels such as email, SMS, and mobile app notifications. To achieve this, you want to implement the Observer pattern, allowing users to subscribe to stock price updates and receive notifications through multiple channels.

Assignment
Your task is to implement the Observer pattern to create a flexible notification system for the stock trading platform. The StockTradingManager class handles stock price updates, and various observer classes (e.g., EmailService, SmsService, AppService) need to be notified when the stock price crosses the threshold.

You need to implement the observer pattern by first defining a method to notify observers in the Observer abstract class. Then, you need to implement the Observer interface and modify the observer classes to receive notifications. The observer side of the pattern is ready.

To implement the publisher side, the registry interface is provided to you through the ObserverRegistry abstract class. You need to implement the methods required by this class in the Publisher class. The Publisher class is a contract that defines the methods that a class can use to add, remove, and notify observers. The StockTradingManager class will implement the Publisher class to notify observers when the stock price crosses the threshold.

Implementing the Observer Pattern
Review the original class: Study the StockTradingManager class and its dependencies. Understand how it currently handles stock price updates and sends notifications.

Complete the observer interface: Design an interface named Observer with a method send_notification that accepts the stock name and current price as arguments. Add this method to the already provided Observer abstract class. This method will be used to notify observers when the stock price crosses the threshold.

Modify the concrete observers: Observer classes (such as EmailService, SmsService, AppService) will implement the Observer interface to receive notifications. Update the existing methods in these classes to match the new interface method signature.

Implement the publisher class: You have been provided with an emptyPublisher class. The publisher class is a contract that defines the methods that a class can use to add, remove, and notify observers. The StockTradingManager class will implement the Publisher class to notify observers when the stock price crosses the threshold. Your task is to first inherit the ObserverRegistry abstract class and then implement the methods defined by this class in the Publisher class. The ObserverRegistry class provides methods to add, remove, and notify observers. You just need to implement these methods in the Publisher class.

Modify the publisher: Refactor the StockTradingManager class as required to implement the Publisher class. The StockTradingManager class should now be able to add, remove, and notify observers. Also modify the method update_stock_price to notify observers when the stock price crosses the threshold.

Test your implementation: Run the provided test cases in the StockTradingManagerTest class to ensure that your observer pattern implementation is correct. These test cases will check if observers are being notified correctly and if the StockTradingManager behaves as expected.

Instructions
Add send_notification method to the Observer abstract class.
Implement the Observer interface in the observer classes (EmailService, SmsService, AppService) to receive notifications.
Inherit the ObserverRegistry abstract class and implement the methods in the Publisher class to add, remove, and notify observers.
Modify the StockTradingManager class to implement the Publisher class and notify observers when the stock price crosses the threshold.
Run the provided test cases in the StockTradingManagerTest class to validate the correctness of your observer pattern implementation. Ensure that observers are being notified correctly and that the StockTradingManager behaves as expected.
'''