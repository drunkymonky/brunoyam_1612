import threading


def foo1():
    for i in range(100):
        print("1")


def foo2():
    for i in range(100):
        print('2')


thread1 = threading.Thread(target=foo1)
thread2 = threading.Thread(target=foo2)

thread1.start()
thread2.start()

# thread1.start()

