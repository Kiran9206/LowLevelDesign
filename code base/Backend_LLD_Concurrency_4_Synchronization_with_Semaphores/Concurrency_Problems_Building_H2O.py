'''
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given
releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier.

These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must
 guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.
We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up
with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into
groups of three, each group should contain one oxygen and two hydrogen threads. Write synchronization code for oxygen and hydrogen molecules
that enforces these constraints.

Example 1
Input: water = "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2
Input: water = "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
Constraints
3 * n == water.length
1 <= n <= 20
water[i] is either 'H' or 'O'.
There will be exactly 2 * n 'H' in water.
There will be exactly n 'O' in water.
'''

import threading

import time
from lib2to3.btm_matcher import type_repr


class H20:

    def __init__(self):
        self.hydrogen = threading.Semaphore(2)
        self.oxygen = threading.Semaphore(1)
        self.lock = threading.Lock()
        self.count = 0
        self.ready = threading.Semaphore(0) #blocking purpose


    def Hydrogen(self):
        if not self.hydrogen.acquire(timeout=2):
            print("Hydrogen thread timed out")
            return
        with self.lock:
            self.count+=1
            if self.count == 3:
                for _ in range(3):
                    self.ready.release()
                self.count = 0
        if not self.ready.acquire(timeout=2):
            print("Hydrogen thread timed out waiting for oxygen")
            self.hydrogen.release()
            return
        releaseHydrogen()
        self.hydrogen.release()

    def Oxygen(self):
        if not self.oxygen.acquire(timeout=2):
            print("Oxygen thread timed out")
            return
        with self.lock:
            self.count+=1
            if self.count == 3:
                for _ in range(3):
                    self.ready.release()
                self.count =0
        if not self.ready.acquire(timeout=2):
            print("Oxygen thread timed out waiting for hydrogen")
            self.oxygen.release()
            return
        releaseOxygen()
        self.oxygen.release()

def releaseHydrogen():
    print('H',end='')

def releaseOxygen():
    print('O',end='')


class H2O_barrier:

    def __init__(self):
        self.hydrogen = threading.Semaphore(2)
        self.oxygen = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)  # Barrier for 3 threads (2 H and 1 O)

    def Hydrogen(self):
        if not self.hydrogen.acquire(timeout=2):
            print("hydrogen get's timed out!!")
            return
        try:
            self.barrier.wait(timeout=2)
            releaseHydrogen()
        except threading.BrokenBarrierError as e:
            print(e)
        finally:
            self.hydrogen.release()

    def Oxygen(self):
        if not self.oxygen.acquire(timeout=2):
            print("Oxygen get's timed out!!")
            return
        try:
            self.barrier.wait(timeout=2)
            releaseOxygen()
        except threading.BrokenBarrierError as e:
            print(e)
        finally:
            self.oxygen.release()


if __name__ == "__main__":
    water = H2O_barrier()
    threads = []
    water_sequence = "HHHHHOOOOOHOHO"  # Example input, can be modified
    print(f"Type of water.hydrogen: {type(water.hydrogen)}")
    print(f"Type of water.oxygen: {type(water.oxygen)}")

    for char in water_sequence:
        if char == 'H':
            t = threading.Thread(target=water.Hydrogen,name="hydrogen_thread")
        else:
            t = threading.Thread(target=water.Oxygen,name="oxygen_thread")

        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()