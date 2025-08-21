'''
Concurrent Counter Management
Problem statement
This Python program is created to implement multithreading concepts. The program has a Counter class with methods to increment, decrement, and retrieve the counter value.
It then creates multiple threads to perform concurrent increment and decrement operations on the counter.

Requirements
Class Counter
Represents a counter object with an initial count.
Provides methods for incrementing, decrementing, and retrieving the counter value.
Methods:
__init__(self, initial_count): Initializes the counter with the specified initial count.
incValue(self, offset): Increments the counter value by the specified offset.
decValue(self, offset): Decrements the counter value by the specified offset.
getValue(self): Retrieves the current value of the counter.
Concurrent Operations
Functions concurrent_inc() and concurrent_dec() perform concurrent increment and decrement operations on the counter.
Each function is executed by multiple threads to simulate concurrent operations.
Instructions
Implement the methods of the Counter class as per the provided TODO comments.
The program will create and start multiple threads for concurrent increment and decrement operations.
After all threads complete execution, the final value of the counter will be printed.
Ensure that the Python environment supports threading to execute the program effectively.
'''

import threading
from concurrent.futures import ThreadPoolExecutor

class Counter:

    def __init__(self, initial_count: int):
        self.initial_count = initial_count
        # Note: In a real-world scenario, you would use threading locks to ensure thread safety.
        self._lock = threading.Lock()


    def inc_value(self, offset: int):
        with self._lock:
            self.initial_count += offset

    def dec_value(self, offset: int):
        with self._lock:
            self.initial_count -= offset

    def get_value(self)-> int:
        return self.initial_count

def concurrent_inc(counter_obj: Counter, offset: int, iterations: int):
    for _ in range(iterations):
        counter_obj.inc_value(offset)

def concurrent_dec(counter_obj: Counter, offset: int, iterations: int):
    for _ in range(iterations):
        counter_obj.dec_value(offset)

if __name__ == "__main__":
    initial_count = 0
    counter = Counter(initial_count)

    thread_result = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Create threads for concurrent increment
        for _ in range(5):
            thread_result.append(executor.submit(concurrent_inc, counter, 1, 1000000))

        # Create threads for concurrent decrement
        for _ in range(5):
            thread_result.append(executor.submit(concurrent_dec, counter, 1, 1000000))

    # Wait for all threads to complete
    for future in thread_result:
        future.result()

    print(f"Final counter value: {counter.get_value()}")






