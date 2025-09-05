'''
Observer Pattern for Stock Trading Platform
Problem Statement
You are developing a stock trading platform where users need to be notified whenever the price of a particular stock crosses
a certain threshold. These notifications should be sent through various channels such as email, SMS, and mobile app notifications.
To achieve this, you want to implement the Observer pattern, allowing users to subscribe to stock price updates and receive notifications
through multiple channels.

Assignment
Your task is to implement the Observer pattern to create a flexible notification system for the stock trading platform.
The StockTradingManager class handles stock price updates, and various observer classes (e.g., EmailService, SmsService,
AppService) need to be notified when the stock price crosses the threshold.

Implementing the Observer Pattern
Review the original class: Study the StockTradingManager class and its dependencies. Understand how it currently handles
stock price updates and notifications.

Implement the publisher interface: You have been provided with a Publisher interface. Your task is to implement the methods
required by this interface in the StockTradingManager class. Remember that the Publisher interface is a contract that defines
the methods that a class can use to notify observers.

Implement the observer interface: Design an interface named Observer with a method that accepts the stock name and current
price as arguments. Observer classes (such as EmailService, SmsService, AppService) will implement this interface to receive notifications.

Modify the publisher: Refactor the StockTradingManager class as required. Do not modify the constructor as it used by the tests.

Modify the observers: Refactor the observer classes to implement the Observer interface. Update their existing methods to match
the new interface method signature.

Test your implementation: Run the provided test cases in the StockTradingManagerTest class to ensure that your observer
pattern implementation is correct. These test cases will check if observers are being notified correctly and if the StockTradingManager
behaves as expected.
'''
from typing import Optional
from abc import ABC, abstractmethod

# step1: Create an Observer interface
class Observer(ABC):

    @abstractmethod
    def update(self, stock_name: str, current_price: float)->Optional[str]:
        pass

# step2: Implement Concrete Observers
class EmailService(Observer):

    def update(self, stock_name: str, current_price: float):
        if current_price >= 100:
            return f"Email: {stock_name} has reached the target price of {current_price}"
        elif current_price <= 50:
            return f"Email: {stock_name} has dropped below the target price of {current_price}"
        return None

class SMSService(Observer):

    def update(self, stock_name: str, current_price: float):
        if current_price >= 100:
            return f"SMS: {stock_name} has reached the target price of {current_price}"
        elif current_price <= 50:
            return f"SMS: {stock_name} has dropped below the target price of {current_price}"
        return None

class AppService(Observer):

    def update(self, stock_name: str, current_price: float):
        if current_price >= 100:
            return f"App Notification: {stock_name} has reached the target price of {current_price}"
        elif current_price <= 50:
            return f"App Notification: {stock_name} has dropped below the target price of {current_price}"
        return None


# step3: Implement the Publisher interface
class Publisher(ABC):
    
    @abstractmethod
    def register(self, observer: Observer):
        pass
    
    @abstractmethod
    def unregister(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self, stock_name: str, current_price: float):
        pass

# step4: Implement the Concrete Publisher

class StockTradingManager(Publisher):
    
    def __init__(self):
        self.observers = []  # List to hold registered observers
    
    def register(self, observer: Observer):
        self.observers.append(observer)
    
    def unregister(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify(self, stock_name: str, current_price: float):
        notification = []
        for observer in self.observers:
            message = observer.update(stock_name, current_price)
            if message:
                notification.append(message)
        return notification



# Example usage:
if __name__ == "__main__":

    stock = StockTradingManager()
    email_service = EmailService()
    sms_service = SMSService()
    app_service = AppService()

    stock.register(email_service)
    stock.register(sms_service)
    stock.register(app_service)
    apple_stock = stock.notify('apple', 120)
    google_stock = stock.notify('google', 40)
    stock.unregister(sms_service)
    microsoft_stock = stock.notify('microsoft', 150)
    tesla_stock = stock.notify('tesla', 30)
    amazon_stock = stock.notify('amazon', 90)
    print( apple_stock)
    print( google_stock)
    print( microsoft_stock)
    print( tesla_stock)
    print( amazon_stock)


