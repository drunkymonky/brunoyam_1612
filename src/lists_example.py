data = [2, 3, 5, 4, 65]
summa = 0
for number in data:
    print(number)
    summa += number

print(summa)
print(sum(data))

zeros = [0, 0] * 15
print(zeros)

print(zeros + data)
# посчитать кол-во положительных элементов в списке
# [1, -3, 2, -3] ->  2
data = [1, 2, 3, -3, 2, -3]
count = 0
for number in data:
    if number > 0:
        count += 1
print(count)
# напечатать все четные элементы из списка
print("--")
data = [1, 2, 3, -3, 2, -3]
for number in data:
    if number % 2 == 0:
        print(number)

# напечатать элементы на четных позициях в списке
for i in range(len(data)):
    if i % 2 == 0:
        print(data[i])
print(data[::2])
# среднее арифметичекое элементов массива
data = [1, 2, 3, -3, 2, -3]
print(sum(data) / len(data))

# напечатать все строки, длина которых больше 5
data = ['hello', 'very long string', 'very very long string']
for value in data:
    if len(value) > 5:
        print(value)

print(ord('a'))
print(chr(97))
symbol = 'b'
upper_symbol = chr(ord(symbol) - 32)
print(upper_symbol)
lower_symbol = chr(ord(upper_symbol) + 32)
print(lower_symbol)

value = 'Hello, world'
result = ''
for symbol in value:
    if 'A' <= symbol <= 'Z':
        result += chr(ord(symbol) + 32)
    elif 'a' <= symbol <= 'z':
        result += chr(ord(symbol) - 32)
    else:
        result += symbol
print(result)


