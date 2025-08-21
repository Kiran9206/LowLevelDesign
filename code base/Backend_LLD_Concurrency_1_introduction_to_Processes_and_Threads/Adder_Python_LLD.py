'''
Multi-threaded Addition Program
Overview
This Python program demonstrates multi-threaded addition functionality using the Client and Adder classes. The program takes two numbers as input
from the user, creates a new thread, and invokes the Adder class to calculate and print the sum of the two numbers.

Implementation Details
Class Adder
Inherits from the threading.Thread class.
Represents a thread that performs addition of two numbers.
Initializes with two numbers (num1 and num2) provided as input.
Overrides the run() method to calculate and print the sum of num1 and num2.
Class Client
Contains a static method main() that serves as the entry point of the program.
Prompts the user to enter two numbers.
Creates an instance of the Adder class with the provided numbers.
Starts the thread and waits for its completion.
Instructions
To run the program:
Execute the Client class's main() method.
Enter two numbers when prompted.
The program will create a new thread to calculate and print the sum of the provided numbers.
Ensure that the program runs in a Python environment with threading support.
'''


import threading


class Adder(threading.Thread):
    def __init__(self, num1: int, num2: int):
        super().__init__()
        self.num1 = num1
        self.num2 = num2


    def run(self):
        result = self.num1 + self.num2
        print(threading.current_thread().name)
        print(f"The sum of {self.num1} and {self.num2} is: {result}")

class Client:
    @staticmethod
    def main():
        try:
            num1 =  int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            return

        adder_thread = Adder(num1, num2)
        adder_thread_2 = Adder(num1, num2)
        adder_thread.start()
        adder_thread_2.start()
        adder_thread.join()
        adder_thread_2.join()

if __name__ == "__main__":
    Client.main()
