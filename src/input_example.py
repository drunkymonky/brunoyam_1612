
while True:
    value = input("Enter expression: ").split()
    if 'exit' in value:
        break
    a = int(value[0])
    # a = input('Введите первое число: ')
    # if a == 'exit':
    #     break
    # a = int(a)
    op = value[1]
    # op = input('Введите операцию:')
    # if op == 'exit':
    #     break
    b = int(value[2])
    # b = input('Введите второе число: ')
    # if b == 'exit':
    #     break
    # b = int(b)
    result = 0
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    print('result = ', result)

