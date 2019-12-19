a = 1  # type: int
b = 2  # type: int
c = 3.8

just_sum = a + b + c
sum_integer = int(just_sum // 3)
sum_decimal = just_sum / 3
print(sum_integer, sum_decimal)

if a > b:
    print(a)
    print('a wins')
else:
    print(b)
    print('b wins')

value = 0
if value < -10:
    print('left')
else:
    if value > 10:
        print('right')
    else:
        print('center')

"""
Here we calculate answer for
problem with three ranges
"""
if value < -10:
    print('left')
elif value > 10:
    print('right')
else:
    print('center')  # some comment

# value in the left part
if value < -10:
    print('left')
if value > 10:
    print('right')
if -10 <= value <= 10:
    print('center')
