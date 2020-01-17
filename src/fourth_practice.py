EMPTY = '___'
data = [EMPTY] * 5

while True:
    user_input = input('Введите команду: ').split()
    command = user_input[0]
    if command == 'show':
        print(data)
    elif command == 'free':
        print(data.count(EMPTY))
    elif command == 'park':
        # free_pos = 0
        # for place in data:
        #     if place == EMPTY:
        #         break
        #     free_pos += 1
        free_pos = data.index(EMPTY)

        data[free_pos] = user_input[1]
        print(data)
    elif command == 'leave':
        # for i in range(len(data)):
        #     if data[i] == user_input[1]:
        #         data[i] = EMPTY
        #         break
        data[data.index(user_input[1])] = EMPTY
        print(data)
    else:
        break
