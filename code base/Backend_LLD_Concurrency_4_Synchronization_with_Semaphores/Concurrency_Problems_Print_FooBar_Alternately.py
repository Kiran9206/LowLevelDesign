'''
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().
Modify the given program to output "foobar" n times.

Example 1:
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
Example 2:
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
Constraints:
1 <= n <= 1000  
'''



import threading

class Foobar:

    def __init__(self,n:int):
        self.n = n
        self.lock = threading.Lock()
        self.foo_sema = threading.Semaphore(1)
        self.bar_sema = threading.Semaphore(0) # Start with foo allowed to print first bar waits..

    def foo(self):
        for _ in range(self.n):
            if not self.foo_sema.acquire(timeout=2):
                print("Foo thread timed out")
                return
            print("foo", end="")
            self.bar_sema.release()

    def bar(self):
        for _ in range(self.n):
            if not self.bar_sema.acquire(timeout=2):
                print("Bar thread timed out")
                return
            print("bar")
            self.foo_sema.release()


if __name__ == "__main__":
    n = 5

    foobar = Foobar(n)

    foo_thread = threading.Thread(target=foobar.foo, name="foo_thread")
    bar_thread = threading.Thread(target=foobar.bar, name="bar_thread")
    foo_thread.start()
    bar_thread.start()
    foo_thread.join()
    bar_thread.join()
    print()  # For a new line after the output
