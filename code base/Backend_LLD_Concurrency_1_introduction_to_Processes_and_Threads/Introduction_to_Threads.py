'''
Raw Problem

**Raw Problem**
Write code to achieve the following
A class Client with main method that prints: I am the main class
Client class should create a new thread and invoke code in a class called Adder.
The Adder class should print: I am the Adder class
Client class should create a new thread and invoke code in a class called Subtractor.
The Subtractor class should print: I am the Subtractor class

Important Note - Use the ScalerThread class to create new threads. This is necessary for testing your code.

'''

import  threading

class Adder:
    def __init__(self):
        pass

    def main(self):
        print("I am the Adder class")


class Subtractor:
    def __init__(self):
        pass

    def main(self):
        print("I am the Subtractor class")


class ScalerThread(threading.Thread):
    def __init__(self,target):
        super().__init__()
        self.target = target

    def run(self):
        self.target.main()


class Client():

    def __init__(self):
        pass

    def main(self):
        print("I'm the main class!")



        # creating thread for adder class
        adder = Adder()
        adder_thread = ScalerThread(target=adder)
        adder_thread.start()

        # creating thread for subtractor class
        subtractor = Subtractor()
        subtractor_thread = ScalerThread(target=subtractor)
        subtractor_thread.start()


        # wait for threads to complete...

        adder_thread.join()
        subtractor_thread.join()
        


if __name__ == '__main__':
    client = Client()
    client.main()






