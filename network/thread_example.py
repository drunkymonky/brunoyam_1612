import threading
import time


def foo1():
    print(time.time())
    for i in range(100000):
        print("1")


def foo2():
    for i in range(100000):
        print('2')


thread1 = threading.Thread(target=foo1)
thread2 = threading.Thread(target=foo2)

# thread1.start()
# thread2.start()

import multiprocessing

if __name__ == '__main__':
    multiprocessing.Process(target=foo1).start()
    print(time.time())
    multiprocessing.Process(target=foo2).start()

# thread1.start()

