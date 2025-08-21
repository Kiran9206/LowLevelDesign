import threading
import time
import os
import concurrent.futures # to creatre the pool for theads..: why?:  creating the threads in a system takes time So, to avoid creating the treads again and again we are using pools
import multiprocessing


def say_hello(T)->None:
    time.sleep(T)
    print("hello",threading.current_thread().name)


# thread1 = threading.Thread(target=say_hello,name="thread1")
# thread2 = threading.Thread(target=say_hello,name="thread2")

# thread1.start()
# thread2.start()



print(f"CPU = {os.cpu_count()}")
t1 = time.perf_counter

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executors:
    executors.submit(say_hello,4)
    executors.submit(say_hello,3)
    executors.submit(say_hello,1)

with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executors:
    executors.submit(say_hello, 4)

process_1 = multiprocessing.Process(target=say_hello,args=(4,))



t2 = time.perf_counter
print(t2-t1)





