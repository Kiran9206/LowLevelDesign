'''
FooBar Printer Challenge
Problem Statement
In this challenge, you are tasked with implementing a multithreaded application that alternates printing the words "foo" and "bar" in
sequence using Python's threading capabilities. The goal is to synchronize two threads to ensure that "foo" and "bar" are printed in the correct
order, forming the sequence "foobar" repeated n times, where n is a given integer.

Task Description
Your task is to implement a class named FooBar that will have two methods: foo and bar. These methods, when executed by different threads,
should print "foo" and "bar" respectively, ensuring that "foo" is always printed before "bar" in each sequence.

Requirements
The class FooBar should accept an integer n in its constructor. This integer n represents the number of times the sequence "foobar" should be
printed.
Implement two methods in the FooBar class:
foo: This method should print the word "foo". It will be called by one thread.
bar: This method should print the word "bar". It will be called by another thread.
Ensure that "foo" and "bar" are printed in the correct sequence, forming "foobar" exactly n times.
Implementation Details
Use Python's threading module to create and manage threads.
Utilize synchronization mechanisms such as semaphores to coordinate the execution order of the threads.
The program should create two threads, one for each method (foo and bar), and start them in such a way that they produce the correct output.
'''

import threading

class FooBar:

    def __init__(self, n: int):
        self.n = n
        self.foo_semaphore = threading.Semaphore(1)
        self.bar_semaphore = threading.Semaphore(0) #waits.....

    def foo(self):
        for _ in range(self.n):
            if not self.foo_semaphore.acquire(timeout=2):
                print("foo_semaphore thread stopped!!")
                return
            print("foo",end="")
            self.bar_semaphore.release()

    def bar(self):
        for _ in range(self.n):
            if not self.bar_semaphore.acquire(timeout=2):
                print("bar semaphore thread stopped!!")
                return
            print("bar")
            self.foo_semaphore.release()


if __name__ == "__main__":
    foobar = FooBar(10)
    t1 = threading.Thread(target=foobar.foo, name="t1")
    t2 = threading.Thread(target=foobar.bar, name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
