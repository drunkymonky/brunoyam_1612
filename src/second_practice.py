# 1
value = 123
if value % 2 == 0:
    print("четное")
else:
    print("нечетное")

# 2
a = 4
b = 6
c = 8
# a b c
if a > b:
    tmp = b
    b = a
    a = tmp
if b > c:
    tmp = c
    c = b
    b = tmp
if a > b:
    tmp = b
    b = a
    a = tmp

print(b)


# 3
a = 14
b = 8
if a % b == 0:
    print("делится")
else:
    print("не делится, остаток =", a % b)
