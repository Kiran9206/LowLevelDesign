'''
You have an object printNumber. printNumber.accept(x) can be called with an integer parameter that prints it to the console.

You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be
passed to three different threads:

Thread A: calls zero() that should only output 0's.
Thread B: calls even() that should only output even numbers.
Thread C: calls odd() that should only output odd numbers.
Modify the given class to output the series "010203040506..." where the length of the series must be 2n.

Implement the ZeroEvenOdd class:

ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
void zero(printNumber) Calls printNumber to output one zero.
void even(printNumber) Calls printNumber to output one even number.
void odd(printNumber) Calls printNumber to output one odd number.
Example 1:
Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.
Example 2:
Input: n = 5
Output: "0102030405"
Constraints:
1 <= n <= 1000
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


