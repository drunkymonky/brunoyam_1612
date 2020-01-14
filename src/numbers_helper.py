

def sum_of_digits(number):
    return sum([int(x) for x in str(number)])


print(sum_of_digits(1234))
print('hello')

number = 123
# подсчитать сумму цифр числа
print(sum([int(x) for x in str(number)]))
number = 123
summa = 0
while number != 0:
    summa += number % 10
    number //= 10
print(summa)

# подсчитать количество делителей
number = 123
count = 0
for i in range(2, number):
    if number % i == 0:
        count += 1
        print(i)
print(count)

print(sum([1 if number % x == 0 else 0 for x in range(2, number)]))


data = [123, 232, 2323]
print('---')
for number in data:
    summa = 0
    while number != 0:
        summa += number % 10
        number //= 10
    print(summa)
print(data)

print('---')
max_sum = -1
for number in data:
    summa = 0
    while number != 0:
        summa += number % 10
        number //= 10
    max_sum = max(max_sum, summa)
print(max_sum)
