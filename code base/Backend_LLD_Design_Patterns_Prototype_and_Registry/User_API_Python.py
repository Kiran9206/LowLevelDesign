'''
Prototype Pattern for Object Cloning in Testing
Problem Statement
You are developing a testing framework for a user API of a social media platform. Each test case requires generating multiple mock users with
different attributes to simulate various scenarios. However, creating mock users for testing involves complex setups and is time-consuming.
To optimize the user creation process during testing, you decide to implement the Prototype pattern. This pattern allows you to create prototype
objects and clone them when needed, avoiding the overhead of setting up complex user objects repeatedly.

Assignment
Your task is to implement the Prototype pattern to create prototype objects for mock users in the testing framework. There is a Cloneable
interface that contains the clone method, which should be implemented by user objects. Additionally, you need to implement a
UserPrototypeRegistry interface that provides methods for adding and retrieving user prototypes and for cloning user objects.
The goal is to simplify the process of creating users with specific attributes.

Implementing the Prototype Pattern
Review the Cloneable interface: Have a look at the interface named Cloneable with a single method, clone_object(), that returns a cloned copy of the
implementing object.

Implement the clone_object() method: Review the User class with attributes for the app. Implement the clone_object() from the Cloneable interface.
Your method should create a new User object and copy the attribute values from the original object to the new object. Return the new object as the
cloned copy. You can either implement the cloning logic or use a library like copy clone the object. You can use any of shallow or deep cop.

Review the UserPrototypeRegistry interface: See the interface named UserPrototypeRegistry that includes methods for adding prototypes,
retrieving prototypes by type, and cloning user objects.

Complete the registry implementation: A class that inherits from the UserPrototypeRegistry interface is present in the codebase. However, the
methods are not implemented. You need to implement the methods to manage user prototypes and perform cloning operations. In this class, manage a
collection of user prototypes and provide methods to add prototypes, retrieve prototypes by type, and clone user objects based on their type.

Instructions
Clone this repository to your local machine.
Implement the Prototype pattern by completing the clone_object() method in the User class.
Implement the UserPrototypeRegistry interface to manage user prototypes and perform cloning operations. Complete the methods in the
UserPrototypeRegistryImpl class.
Run the provided test cases in the TestUserPrototypeRegistryImpl class to validate the correctness of your prototype pattern implementation.
Ensure that user objects can be cloned successfully, and that the registry functions as expected.
'''