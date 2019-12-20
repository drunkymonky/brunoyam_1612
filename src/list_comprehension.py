a = 10
b = 20
values = [x ** 2 for x in range(a, b + 1)]

# values = []
# for x in range(a, b + 1):
#     values.append(x ** 2)
print(values)

values = [x for x in values if x % 2 == 0]
print(values)

values = [100 if x < 200 else 400 for x in values]
print(values)

# сгенерировать списко чисел от А до В
print([x for x in range(a, b + 1)])
# сгенерировать список степеней двойки от 0 до n
# [1, 2, 4, 8, 16, 32, 64, ..]
n = 100
power_of_two = [2 ** i for i in range(n)]
print(power_of_two)

# оставить в списке только строки полностью в верхнем регистре
value = 'DFDF'
upper_case = value.upper()  # 'ABC'
print(value, upper_case)
values = ['HELLO', 'world']
values = [x for x in values if x == x.upper()]
values = [x for x in values if x.isupper()]
print(values)
#* сгенерировать список вида [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...]
