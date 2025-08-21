'''
Raw Problem

**Raw Problem**
Write code to achieve the following
A class Client with a main method.
Client class shall take two numbers as input from the user.
Client class should create a new thread and invoke code in a class called Adder.
Client class shall pass two numbers (taken as input from the user) to the Adder class.
The Adder class should print the sum of two numbers passed to it.

Important Note - Use the ScalerThread class to create new threads. This is necessary for testing your code.
'''

import threading
class ScalerThread(threading.Thread):
    def __init__(self, target):
        super().__init__()
        self.target = target

    def run(self):
        self.target.main()


class Adder:

    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2

    def main(self):
        print(f"sum is : {self.num1 + self.num2}")


class Client:

    def __init__(self):
        self.num1 = int(input())
        self.num2 = int(input())

    def main(self):


        adder = Adder(self.num1, self.num2)
        adder_thread = ScalerThread(target=adder)
        adder_thread.start()
        # Ensuring the main thread waits for the adder thread to finish
        adder_thread.join()

if __name__ == "__main__":
    client = Client()
    client.main()

