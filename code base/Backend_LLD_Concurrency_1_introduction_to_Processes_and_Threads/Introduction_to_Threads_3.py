'''
Raw Problem

**Raw Problem**
Write code to achieve the following
A class Client with a main method.
Client class shall take a number n as input.
A class called TableCreator which prints the multiplication table from 1 to 10 for a given number x
x times 1 is x

..

x times 10 is 10x
Client should create a thread for every number between 1 to n, n included and
Pass it to TableCreator to print a multiplication table for that number.
Print format = 2 times 6 is 12
'''
import threading
from concurrent.futures import ThreadPoolExecutor

class TableCreator:
    def __init__(self, x):
        self.x = x

    def main(self):
        for idx in range(1,11):
            print(f"{self.x} times {idx} is {idx * self.x} : {threading.currentThread().name}")
        print()

class Client:

    def __init__(self):
        pass

    def main(self):
        n = int(input("Enter a number : "))

        with ThreadPoolExecutor(max_workers=n) as executor:
            futures = []
            for idx in range(1, n+1):
                table_creator = TableCreator(idx)
                futures.append(executor.submit(table_creator.main))

        for future in futures:
            future.result()


if __name__ == '__main__':
    client = Client()
    client.main()




