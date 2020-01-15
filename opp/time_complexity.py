import time


def first():
    a = 1
    b = 2
    print(a + b)


def second(n):
    summa = 0
    for i in range(1, n):
        summa += i
    for i in range(1, n):
        summa -= i


def third(n):
    pairs = []
    for i in range(n):
        for j in range(n):
            pass


def bubble_sort(data):
    n = len(data)
    for i in range(n):  # длина текущего куска n - i
        for j in range(0, n - i - 1):  # [0, n], [0, n -1], [0, n - 2]
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print(data)


def python_sort(data):
    print(sorted(data))


def run_timed(fun, *args):
    begin_time = time.time()
    fun(*args)
    end_time = time.time()
    print(end_time - begin_time)
    return end_time - begin_time


linear_result = []
quadr_result = []
for n in range(100, 600, 1):
    linear_result.append(run_timed(second, n))
    quadr_result.append(run_timed(third, n))

print(linear_result)
print(quadr_result)


# run_timed(first)
# run_timed(second)
# run_timed(third)

import random

numbers = []
numbers_for_python = []
n = 10000
for i in range(n):
    current_number = random.randint(0, 100000000)
    numbers.append(current_number)
    numbers_for_python.append(current_number)

# run_timed(bubble_sort, numbers)
# run_timed(python_sort, numbers_for_python)
