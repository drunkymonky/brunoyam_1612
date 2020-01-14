def walk(x, y):
    if x == 4:
        return
    print(x, y)
    walk(x + 1, y)


def fact(n):  # n!
    if n == 1:
        return 1
    return fact(n - 1) * n  # = (n-1)! * n


fact(4)

 walk(0, 0)