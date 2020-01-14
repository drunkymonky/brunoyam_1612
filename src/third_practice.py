# 1
values = []
k = 10
n = 4
for k in range(1, n + 1):
    for i in range(k):
        values.append(k)
print(values)

values = [k for k in range(1, n + 1) for i in range(k)]
print(values)

for k in range(1, n + 1):
    values += [k] * k
    # print(values)

# 2
n = 5
m = 5
bomb = 9
data = [[0 for i in range(n)] for j in range(m)]
# data[0][1] = bomb
data[2][3] = bomb
# data[2][1] = bomb
print(data)
x = 1
y = 1
data.insert(0, [0] * (n + 2))  # строчка в начале
data.append([0] * (n + 2))  # строчка в конце
for i in range(1, m + 1):  # строки между
    data[i].append(0)
    data[i].insert(0, 0)
print(data)
# смещаем точку в новом поле
x += 1
y += 1
bomb_count = 0
for i in range(-1, 2):
    for j in range(-1, 2):
        if data[x + i][y + j] == bomb:
            bomb_count += 1
print(bomb_count)

for row in range(m):
    for column in range(n):
        x = row + 1
        y = column + 1
        if data[x][y] != bomb:
            bomb_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if data[x + i][y + j] == bomb:
                        bomb_count += 1
            data[x][y] = bomb_count

for row in data:
    print(row)

# 3
result = []
n = 7
for i in range(n):
    current_list = [x for x in range(n * i + 1, n * (i + 1) + 1)]
    if i % 2 == 1:
        current_list.reverse()
    result.append(current_list)

for row in result:
    print(row)

# 4
x = 0
y = 0
direction = 0
n = 3
result = [[0 for i in range(n)] for j in range(n)]
current = 1
# for value in range(1, n * n + 1):
while current < n * n + 1:
    # print(x, y, current)
    if result[x][y] == 0:
        result[x][y] = current
        current += 1

    if direction == 0:  # движение вправо
        if y + 1 < n and data[x][y + 1] == 0:
            # print('go right')
            y += 1
        else:
            # print('change to left')
            direction += 1  # идем вниз
    elif direction == 1:  # движение вниз
        if x + 1 < n and data[x + 1][y] == 0:
            x += 1
        else:
            direction += 1  # идем влево
    elif direction == 2:  # движение влево
        if y - 1 >= 0 and data[x][y - 1] == 0:
            y -= 1
        else:
            direction += 1  # идем вверх
    elif direction == 3:  # движение вверх
        if x - 1 >= 0 and data[x - 1][y] == 0:
            # print('go up')
            x -= 1
        else:
            # print('change to right')
            direction = 0  # движение вправо
    print(result)

for row in result:
    print(row)
