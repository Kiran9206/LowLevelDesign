'''
Print in Order Challenge
Problem Statement
In this challenge, you are required to ensure that three different methods print in strict sequence: "first", "second", and "third". You are given a class Foo with three methods:

first(): prints "first"
second(): prints "second"
third(): prints "third"
Your task is to modify the Foo class to ensure that these methods can only run in sequence (first, then second, then third), regardless of the order in which they're called in the code.

Requirements
The class Foo is already provided with semaphore placeholders for synchronization.
You need to initialize any required semaphores in the __init__ method of the Foo class.
Implement the first, second, and third methods using semaphores to enforce the correct sequence of execution.
The output list attribute of the Foo class should collect the strings "first", "second", and "third" in the exact order of method execution to validate the sequence.
Implementation Details
Use Python's threading module for thread creation and synchronization.
Leverage semaphores from the threading module to enforce the execution order of first(), second(), and third() methods.
'''

import threading

class Foo:

    def __init__(self):
        self.first_sema = threading.Semaphore(1)
        self.second_sema = threading.Semaphore(0)
        self.third_sema = threading.Semaphore(0)

    def first(self):
        if not self.first_sema.acquire(timeout=2):
            print("Timeout waiting for first semaphore")
            return
        print("first")
        self.second_sema.release()

    def second(self):
        if not self.second_sema.acquire(timeout=2):
            print("Timeout waiting for second semaphore")
            return
        print("second")
        self.third_sema.release()

    def third(self):
        if not self.third_sema.acquire(timeout=2):
            print("Timeout waiting for third semaphore")
            return
        print("third")
        self.first_sema.release()


if __name__ == "__main__":
    foo =Foo()
    t1 = threading.Thread(target=foo.first, name="t1")
    t2 = threading.Thread(target=foo.second, name="t2")
    t3 = threading.Thread(target=foo.third, name="t3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()