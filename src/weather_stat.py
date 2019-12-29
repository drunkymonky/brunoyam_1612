# Y:\Python-1785\brunoyam_1612_git


def number_of_days(month_number):
    if month_number == 1:  # feb
        return 28
    else:
        if month_number < 7:  # jan - jul
            return 30 if month_number % 2 == 1 else 31
        else:  # aug - dec
            return 31 if month_number % 2 == 1 else 30


weather = dict()
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
for i in range(len(months)):
    current_month = months[i]
    weather[current_month] = [0] * number_of_days(i)


with open("../data_one_year.txt", "r") as data:
    for month in months:
        current_days = weather[month]
        for i in range(len(current_days)):
            current_days[i] = int(data.readline())

print(weather['apr'][23])


def process_average(user_input):
    if len(user_input) > 2:
        first = user_input[1]
        second = user_input[2]
        # TODO: посчитать среднее для нескольких месяцев
    elif user_input[1] == 'year':
        summa = 0
        for month in weather:
            summa += sum(weather[month])
        print(summa / 365)
    else:
        days = weather[user_input[1]]
        print(sum(days) / len(days))


def process_command(user_input, year_process, month_process, range_process):
    if len(user_input) > 2:
        range_process(user_input)
    elif user_input[1] == 'year':
        year_process(user_input)
    else:
        month_process(user_input)


def year_process_average(user_input):
    first = user_input[1]
    second = user_input[2]
    # TODO: посчитать среднее для нескольких месяцев


def month_process_average(user_input):
    pass


def range_process_average(user_input):
    pass

average_of_list = lambda data: sum(data) / len(data)
print(average_of_list([1, 2, 3]))


while True:
    try:
        user_input = input().split()
        command = user_input[0]

        if command == 'temp':
            month = user_input[1]
            day = int(user_input[2])
            print(weather[month][day])
        elif command == 'average':
            process_average(user_input)
        elif command == 'min':
            pass
            # process_command(user_input)
    except:
        print("Wrong command. Retry")
    # except ValueError:
    #     pass
    # except




















