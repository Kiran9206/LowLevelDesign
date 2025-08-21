'''
Builder Pattern Implementation for a messaging service
Problem Statement
You are developing a messaging application with support for various message types, including text, images, audio, and video.
Each message type can have additional attributes and settings, such as delivery status and timestamps. The current approach of
creating message objects using multiple overloaded constructors has become error-prone and challenging to maintain. You should
streamline the creation of message objects with different configurations and immutable objects.

Assignment
Your task is to implement the Builder pattern to create instances of message objects with different configurations. The Builder pattern
allows for step-by-step construction of complex objects while keeping the creation process separate from the main object.

The usage of your builder should look like this:

message = MessageBuilder()\
    .with_type('text')\
    .with_content('Hello, World!')\
    .with_recipient('example@example.com')\
    .build()
Implementing the Builder Pattern
Review the original class and the builder interface - You have been provided with a class that represents the message data Message.
The class has a number of properties that are used to create the message object. The class extends from the Builder interface which has a method
build() that returns an instance of the class. Your task is to implement the Builder pattern to create instances of a class with the same properties.
You have to complete the implementation of the build method.

Implement the setter methods - The idea of the builder method to have a mutable instance of the Message class in the builder class and expose
methods to set the properties of the class. Once the properties have been set, the build method is called to create an immutable instance of the class.
 You need to implement the setter methods for the properties of the Message class in the builder class. Methods like with_type, with_content,
 with_recipient, etc. should be implemented so that the user can use the builder instance to set the properties of the Message class.

Implement the build method - The build method is responsible for creating an instance of the Message class. The method should return an instance of
the Message class with the properties set by the user using the builder instance.

Test your implementation - A test case has been provided for you to test your implementation. Run the test case to ensure that your implementation is
correct.

Instructions
Clone this repository to your local machine.
Open the Message class and implement the setter methods in the MessageBuilder class.
Implement the build method in the MessageBuilder class.
Run the provided test cases in the TestMessageBuilder class to verify the correctness of your implementation.
'''