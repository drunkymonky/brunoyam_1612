from typing import List


def sum_of_two_element(a, b):
    """
    Функция для вычисления суммы двух чисел

    :param a: первое число для суммы
    :type a: int
    :param b: второе число для суммы
    :type b: int
    :return: сумма двух чисел
    :rtype: int
    """
    return a + b


print(sum_of_two_element(1, 2))
print(sum_of_two_element(4, 2))


def find_positive_elements(data):
    """
    :type data: List[int]
    """
    result = []
    for element in data:
        if element > 0:
            result.append(element)
    return result


print(find_positive_elements([1, -2, 3, -5]))


def my_join(*args, delimiter=' '):
    return delimiter.join(args)


print(my_join('Hello', 'world', 't', 't', 't', 't'))
print(my_join('a', 'b', 'c', 'd', delimiter=', '))

print('hello', 'world', '!', sep=', ', end='!!!\n')


def most_common_function(*args, **kwargs):
    print(args)
    print(kwargs)


most_common_function('hello', 'world', '!', sep=', ', end='!!!')


# 1 максимум из трех чисел
def max_of_three(a, b, c):
    # return max(a, b, c)
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    return c


print("\nTasks")
print(max_of_three(1, 2, 3))


# 2 дан год (число), определить, является ли он високосным (либо делится на 4 и не делится на 100)
def is_vic(year):
    if year % 4 == 0 and year % 100 != 0:
        return 'Yes'
    else:
        return 'No'


print(is_vic(2020))
print(is_vic(1900))
print(is_vic(2001))


# 3 даны длины двух катетов прямоугольного треугольника, посчитать гипотенузу
# c = sqrt(a^2 + b^2)
def hip(a, b):
    return (a ** 2 + b ** 2) ** 0.5


print(hip(3, 4))
print(hip(14, 13))


# 4 проверить, что число является простым (делится без остатка) только на 1 и на себя)
# 7?    2 3 4 5 6
def is_prime(number):
    result = True
    for i in range(2, number):
        if number % i == 0:
            result = False
            break
            # return 'No'
    return 'Yes' if result else 'No'


print(is_prime(10))
print(is_prime(7))












