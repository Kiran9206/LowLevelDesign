'''
Facade pattern for image editing application
Problem Statement
You are developing an image editing software that offers various features like loading images, applying filters, adjusting brightness,
and saving images. The editing module has complex interactions and dependencies. Your goal is to simplify the interface for users by providing a
unified way to access and control these editing functionalities.

Assignment
Your task is to implement the Facade pattern to refactor the existing ImageEditingManager class. The class currently handles image editing
functionalities separately. Your objective is to implement a facade class that presents a unified and simplified interface for users to perform image
editing tasks while abstracting away the internal complexities.

Implementing the Facade Pattern
Review the original class: Take a closer look at the ImageEditingManager class and its methods. Understand the dependencies it uses and the interactions
with external services.

Complete the facade class: Complete the new class called ImageProcessor that implements the Facade pattern. This class will encapsulate the complex
interactions with the external services and provide a simplified interface for clients.

Remember to call the constructor of your facade using the same arguments from the BookingManager class: The constructor of your ImageProcessor class
should take the same arguments that the ImageEditingManager class constructor does. This allows you to pass the necessary dependencies to the facade.

Test your implementation: Test cases have been provided for you to test your implementation. Run the test cases to ensure that your facade class
works correctly and provides the expected functionality.

Instructions
Complete the new class named ImageProcessor.
Implement the Facade pattern within your ImageProcessor class to encapsulate interactions with external services.
Ensure that your ImageProcessor constructor takes the same arguments as the ImageEditingManager constructor.
Run the provided test cases in the TestImageEditingManager class to verify the correctness of your implementation.
'''