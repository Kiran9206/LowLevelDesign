'''
Builder Pattern Implementation for a messaging service
Problem Statement
You are developing a messaging application with support for various message types, including text, images, audio, and video. Each message type
 can have additional attributes and settings, such as delivery status and timestamps. The current approach of creating message objects using
 multiple overloaded constructors has become error-prone and challenging to maintain. You should streamline the creation of message objects with
 different configurations and immutable objects.

Assignment
Your task is to implement the Builder pattern to create instances of message objects with different configurations. The Builder pattern allows for
step-by-step construction of complex objects while keeping the creation process separate from the main object.

Implementing the Builder Pattern
Review the original class: You have been provided with a class named Message. This class represents different message types and their attributes.
Your task is to implement the Builder pattern to create instances of a class with the same properties.

Create the builder class: Create a new class called MessageBuilder that will implement the builder patter. A dummy class has been provided for you to
start with. Remember to annotate the class with the @WithBuilder annotation. The name does not matter as long as it is annotated.

Test your implementation: Test cases has been provided for you to test your implementation. Run the test case to ensure that your implementation is
correct.
'''


# step1: identify the complex object to be built -> Message class
# step2: create a concrete product class -> Message

class WithBuilder:
    pass

class Message:

    def __init__(self, message_type: str, content: str, status: str, timestamp: str):
        self._message_type = message_type
        self._content = content
        self._status = status
        self._timestamp = timestamp

    @property
    def message_type(self):
        return self._message_type
    @property
    def content(self):
        return self._content
    @property
    def status(self):
        return self._status
    @property
    def timestamp(self):
        return self._timestamp

    def __str__(self):
        return f"Message(type={self._message_type}, content={self._content}, status={self._status}, timestamp={self._timestamp})"

# step3: create a builder class -> MessageBuilder

# @WithBuilder
class MessageBuilder:

    def __init__(self):
        self._message_type = None
        self._content = None
        self._status = "pending"
        self._timestamp = None


    def set_message_type(self, message_type: str):
        self._message_type = message_type
        return self

    def set_content(self, content: str):
        self._content = content
        return self

    def set_status(self, status: str):
        self._status = status
        return self

    def set_timestamp(self, timestamp: str):
        self._timestamp = timestamp
        return self

    def build(self) -> Message:
        if not self._message_type or not self._content or not self._timestamp:
            raise ValueError("Message type, content, and timestamp are required.")
        return Message(
            message_type=self._message_type,
            content=self._content,
            status=self._status,
            timestamp=self._timestamp
        )

# step4: test the builder pattern implementation
class Client:

    def __init__(self):
        self.Builder = MessageBuilder()

    def create_massage(self, message_type: str, content: str, status: str, timestamp: str) -> Message:
        return (self.Builder
                .set_message_type(message_type)
                .set_content(content)
                .set_status(status)
                .set_timestamp(timestamp)
                .build())

# Example usage
import datetime
if __name__ == "__main__":
    client = Client()
    txt = client.create_massage(message_type="text", content="Hello this a simple text message", status="initiated", timestamp=datetime.time())
    image = client.create_massage(message_type="image", content="Image content here", status="sent", timestamp=datetime.time())
    audio = client.create_massage(message_type="audio", content="Audio content here", status="pending", timestamp=datetime.time())
    print(txt)
    print(image)
    print(audio)
