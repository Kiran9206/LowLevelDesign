'''
Zero Even Odd Challenge
Problem Statement
In this challenge, you are required to design a multithreading solution that ensures the ordered printing of numbers in a zero-even-odd sequence up to a given n. Specifically, you'll be working with a class ZeroEvenOdd that provides three methods:

zero(printNumber): prints "0" to the standard output.
even(printNumber): prints even numbers to the standard output.
odd(printNumber): prints odd numbers to the standard output.
Each of these methods is intended to be executed by a different thread.

Task Description
Your task is to implement the ZeroEvenOdd class to ensure that:

The zero method prints "0" and is called n times.
The even method prints even numbers from 2 to n.
The odd method prints odd numbers from 1 to n.
The numbers are printed in sequence, with "0" printed between each number, resulting in a pattern like "0102030405" for n = 5.
Requirements
Utilize semaphores from Python's threading module to synchronize the execution order of zero, even, and odd methods.
The PrintNumber class is provided to encapsulate the logic for printing numbers and should be used as is.
Ensure your implementation allows the threads to cooperate smoothly, maintaining the correct sequence regardless of how they are scheduled by the Python interpreter.
Implementation Details
The ZeroEvenOdd class constructor accepts an integer n, representing the maximum number to print.
You need to correctly initialize and use semaphores to control the execution flow between the threads running zero, even, and odd methods.
'''

from concurrent.futures import ThreadPoolExecutor
import threading

class ZeroEvenOdd:

    def __init__(self, n):
        self.n = n
        self.zero_sema = threading.Semaphore(1)
        self.odd_sema = threading.Semaphore(0) #waits...
        self.even_sema = threading.Semaphore(0) #waits...

    def zero(self, printnumbers):
        for idx in range(1,self.n+1):
            if not self.zero_sema.acquire(timeout=2):
                print("zero thread stopped!!")
                return
            printnumbers(0)
            if idx % 2 == 0:
                self.even_sema.release()
            else:
                self.odd_sema.release()

    def even(self, printnumbers):
        for idx in range(2, self.n+1, 2):
            if not self.even_sema.acquire(timeout=2):
                print("even thread stopped!!")
                return
            printnumbers(idx)
            self.zero_sema.release()

    def odd(self, printnumbers):
        for idx in range(1, self.n+1, 2):
            if not self.odd_sema.acquire(timeout=2):
                print("odd thread stopped!!")
                return
            printnumbers(idx)
            self.zero_sema.release()

def printNumber(x:int):
    print(x,end="")


if __name__ == "__main__":
    n = 10
    ZeroEvenOdd = ZeroEvenOdd(10)
    threads = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        threads.append(executor.submit(ZeroEvenOdd.zero, printNumber))
        threads.append(executor.submit(ZeroEvenOdd.even, printNumber))
        threads.append(executor.submit(ZeroEvenOdd.odd, printNumber))

    for thread in threads:
        thread.result()