

def short_name(first_name, last_name, family_name):
    return last_name + " " + first_name[0] + ". " + family_name[0] + "."


print(short_name("Ivan", "Ivanov", "Ivanovich"))


def is_sorted(data):
    ordered = sorted(data)
    if ordered == data:
        return True
    ordered.reverse()
    # ordered = reversed(ordered)
    if ordered == data:
        return True
    return False


data = [1, 2, 3]
print(is_sorted(data))
data.reverse()
print(is_sorted(data))
data[0] = 0
print(is_sorted(data))


def distinct(data):
    # elements = set(data)
    # for value in data:
    #     elements.add(value)
    data[0] = 12
    return list(set(data))


values = [1, 2, 3, 3]
print(distinct(values))
print(values)


def form_map(names, phones):
    name_to_phone = dict()
    for i in range(len(names)):
        name_to_phone[names[i]] = phones[i]
    return name_to_phone


