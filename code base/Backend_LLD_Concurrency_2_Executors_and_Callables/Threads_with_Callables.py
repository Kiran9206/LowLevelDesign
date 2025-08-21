'''
Raw Problem

Write code to achieve the following
A class Client with a main method.
Create a class ArrayCreator which takes as input a number (n)
ArrayCreator should create an ArrayList which should contain numbers from 1 to n
ArrayCreator should implement appropriate Callable interface and return the arraylist discussed above to calling thread
Client class should invoke ArrayCreator over a new thread and get the arraylist from ArrayCreator class and print it.
'''


import threading
from concurrent.futures import ThreadPoolExecutor

class ArrayCreator:
    def __init__(self, n):
        self.n = n

    def callable(self):
        array_list = [i for i in range(1, self.n+1)]
        return array_list


class Client():

    def __init__(self,n):
        self.n = n

    def main(self):
        array_creator = ArrayCreator(self.n)
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(array_creator.callable)
            print(future.result())

if __name__ == "__main__":
    client = Client(10)
    client.main()
    print("Array created successfully.")