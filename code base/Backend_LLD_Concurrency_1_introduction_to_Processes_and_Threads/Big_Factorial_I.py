'''
Big Factorial (Assignment)
Problem Statement
Implement a thread that computes factorials of a large number. Since the result can be significantly large, you should use the BigInteger class
to store the result and perform the computation.

Instructions
Implement the BigFactorial Class: Design this class to utilize multi-threading for computing the factorial of large numbers, specifically by
extending the Thread class. Incorporate the BigInteger class for handling large results. Detailed requirements for the class include:
An int field to hold the number for factorial computation.
A BigInteger field to store the computed factorial.
A constructor to initialize the class with the target number.
Essential methods to perform the computation in a separate thread and retrieve the result.
The class should override the run() method of the Thread class to perform the factorial computation within a separate thread.
The class should efficiently calculate the factorial of any number provided, ensuring thread-safe execution and resource management, by extending the
Thread class and overriding the run() method.
'''



import threading

class BigFactorial(threading.Thread):

    def __init__(self, number: int):
        super().__init__()
        self.number = number
        self.factorial_result = 1


    # calculate the factorial of the number by recursion
    def calculate_factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calculate_factorial(n-1)

    def run(self):
        self.factorial_result = self.calculate_factorial(self.number)
        print(f"Factorial of {self.number} is {self.factorial_result}")



if __name__ == "__main__":
    number = 5
    big_factorial_thread = BigFactorial(number)
    big_factorial_thread_2 = BigFactorial(number + 1)  # Example with another number
    big_factorial_thread.start()
    big_factorial_thread_2.start()
    big_factorial_thread.join()
    big_factorial_thread_2.join()
    print(f"Thread {big_factorial_thread.name} has completed execution.")
    print(f"Thread {big_factorial_thread_2.name} has completed execution.")


