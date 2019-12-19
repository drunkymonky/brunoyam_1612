name = 'Svetozar'

print(name[0])
print(type(name[3]))

subname = name[1:3]
print(subname)

subname = name[1:]
print(subname)

subname = name[:4]
print(subname)

print(name[::2])

print(name[-1])
print(name[-8])

print(name[0:8])

print(name[::-1])

value = 'abcdeeeeef'
symbol = 'e'

count = 0
for char in value:
    if char == symbol:
        count += 1  # count = count + 1

print('number of elements', count, (count / len(value)) * 100)

count = 0
for i in range(len(value)):
    char = value[i]

    print(i, char)
    if char == symbol:
        count += 1

print('number of elements', count, (count / len(value)) * 100)

# Дана строка, поменять в ней первый и последний символ
# 'abcde' -> 'ebcda'
value = 'abccccbbcca'
print(value[-1] + value[1:-1] + value[0])

# Проверить, что строка состоит только из символов 'a', 'b', 'c'
# 'abc' -> yes
# 'aberdf' -> no
result = True
for char in value:
    if char not in 'abc':  # if char != 'a' or char != 'b' or char != 'c':
        result = False
        break
print(value, ' consists of abc', result)

# Проверить симметрию относительно середины строки (палиндром)
# 'abcba' -> yes
# 'abbb' -> no
value = 'abcba'
result = True
for i in range(len(value)//2):
    if value[i] != value[-i - 1]:
        result = False
        break

print(result)
print(value == value[::-1])


# Сжать строку по правилу: все последовательности повторяющихся символов длины больше 1 заменить на символ + кол-во повторений
# 'aaabbbb' -> 'a3b4'
# распечатать цепочки повторяющихся символов
value = 'aaaabbbcc' + '$'
last_change = 0
result = ''
for i in range(len(value) - 1):
    if value[i] != value[i + 1]:
        current_value = value[last_change: i + 1]
        result += value[i] + str(len(current_value))
        last_change = i + 1
print(result)






