'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering.
The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(),
and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
Constraints:
nums is a permutation of [1, 2, 3].

'''


import threading

class Foo:

    def __init__(self, nums):
        self.nums = nums
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
    nums = [1,3,2]
    foo =Foo(nums)

    method_map = {
        1: foo.first,
        2: foo.second,
        3: foo.third
    }

    threads = []
    for num in nums:
        thread = threading.Thread(target=method_map[num],name=f"Thread-{num}")
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
