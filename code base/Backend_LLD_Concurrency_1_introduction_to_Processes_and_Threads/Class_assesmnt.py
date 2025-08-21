import threading

def print_number(number:int):
    print(f"{number}: {threading.currentThread().name}")

for i in range(1,101):
    thread = threading.Thread(target=print_number, args=(i,))
    thread.start()