'''
Raw Problem

Create a class with the following requirements

Class should be public and name is Counter
It should’ve a single private data member of int type named count
It should’ve a single public constructor which takes an integer parameter and sets the value of count
It should’ve following 3 methods
public void incValue(int offset)

This method should increment the value of count by offset. Also make this method synchronized

public void getValue()

This method should return the value of count. Also make this method synchronized

public void decValue(int offset)

This method should decrement the value of count by offset. Also make this method synchronized
'''
import threading


class Counter:

    def __init__(self, initial_count: int):
        self.__count = initial_count
        self.__lock = threading.Lock()

    def inc_value(self, offset: int)-> None:
        with self.__lock:
            self.__count+=offset

    def get_value(self)-> int:
        with self.__lock:
            return self.__count

    def dec_value(self, offset: int)-> None:
        with self.__lock:
            self.__count -= offset

