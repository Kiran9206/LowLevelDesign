'''
Observer Pattern for Task Management Application
Problem Statement
You are building a task management application where users can create tasks and assign them to different team members.
To enhance the user experience, Joe, a developer on your team, wants to implement a feature where team members receive
notifications whenever they are assigned a new task. These notifications should be sent through various communication
channels, such as in-app alerts, emails, and Slack messages. Joe believes that implementing the Observer pattern will
provide a flexible and maintainable solution for this requirement.

Assignment
Your assignment is to implement the Observer pattern to create a flexible notification system for the task management
application. The TaskManager class handles task assignments, and various observer classes (e.g., AlertService, EmailService, SlackService)
need to be notified when a new task is assigned to a team member.

Implementing the Observer Pattern
Understand the original class: Take a closer look at the TaskManager class and its interactions with the task database
and notification services. Understand how tasks are assigned and notifications are sent.

Implement the observer interface: Implement the interface named Observer with a method that accepts the task and the
team member as arguments. Observer classes (such as AlertService, EmailService, SlackService) will implement this
interface to receive notifications.

Implement the publisher interface: You have been provided with a Publisher abstract class. Your task is to implement the
methods required by this interface in the TaskManager class. The Publisher interface defines methods that allow observers
to subscribe and unsubscribe.

Modify the observers: Refactor the observer classes to implement the Observer interface. Update their existing methods
to match the new interface method signature.

Modify the publisher: Refactor the TaskManager class as required. Implement the publisher methods to manage observer
subscriptions and notify observers when a task is assigned.

Test your implementation: Run the provided test cases in the TaskManagerTest class to ensure that your observer pattern
implementation is correct. These test cases will check if observers are being notified correctly and if the TaskManager
behaves as expected.
'''

from abc import ABC, abstractmethod
# step1: create observer interface

class Observer(ABC):
    @abstractmethod
    def update(self, task: str, team_member: str)->str:
        pass

# step2: create concrete observer

class AlertService(Observer):

    def update(self, task: str, team_member: str)->str:
        return f"Alert: New task '{task}' assigned to {team_member}"

class EmailService(Observer):

    def update(self, task: str, team_member: str)->str:
        return f"Email: New task '{task}' assigned to {team_member}"

class SlackService(Observer):

    def update(self, task: str, team_member: str)->str:
        return f"Slack: New task '{task}' assigned to {team_member}"

# step3: create publisher interface

class Publisher(ABC):

    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, task: str, team_member: str):
        pass

# step4: create concrete publisher

class TaskManager(Publisher):

    def __init__(self):
        self.observers = []

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, task: str, team_member: str):
        notification = []
        for observer in self.observers:
            message = observer.update(task, team_member)
            if message:
                notification.append(message)
        return notification

# step5: testcases

if __name__ == "__main__":

    task_manager = TaskManager()

    alert_service = AlertService()
    email_service = EmailService()
    slack_service = SlackService()

    task_manager.subscribe(alert_service)
    task_manager.subscribe(email_service)
    task_manager.subscribe(slack_service)
    notifications = task_manager.notify("Complete project documentation", "Alice")
    print(notifications)
    task_manager.unsubscribe(alert_service)
    notifications = task_manager.notify("Prepare for client meeting", "Bob")
    print(notifications)