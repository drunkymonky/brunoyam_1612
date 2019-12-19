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
# напечатать элементы на четных позициях в списке
for i in range(len(data)):
    if i % 2 == 0:
        print(data[i])
print(data[::2])
# среднее арифметичекое элементов массива

# напечатать все строки, длина которых больше 5
