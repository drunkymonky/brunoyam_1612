import time


def run_with_time(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


def common_function(*arg, **kw):
    pass


@run_with_time
def action(name):
    print(name)
    return [i for i in range(10000000)]

# start_time = time.time()
# action()
# end_time = time.time()
# print(end_time - start_time)
# run_with_time(action)('hello')
action('hello')  # run_with_time(action)('hello')
