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
    proc1 = multiprocessing.Process(target=foo1)
    proc1.start()
    print(time.time())
    proc2 = multiprocessing.Process(target=foo2)
    proc2.start()

    proc1.join()
    proc2.join()



# thread1.start()

