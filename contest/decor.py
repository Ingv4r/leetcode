import time, typing
from decimal import Decimal


def time_checker(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        stop = time.perf_counter() - start
        time_res = Decimal(stop)
        return f'Function result: {res} \nTime is: {time_res:.^2}'
    return wrapper


@time_checker
def sum_numbs(x, y):
    return x + y

print(sum_numbs(10, 20))

class SomeClass:
    def __init__(self, val):
        self.val = val


d = {
    'a': 123,
    'b': 0,
    'c': -1,
    'd': 1415
}






def biggest_keys(d):
    res = sorted(d, key=lambda x: d[x])
    return res[:2]


def key_of_val(val, d: dict):
    for key, dict_val in d.items():
        if val == dict_val:
            return key



print(key_of_val(90, d))
print(biggest_keys(d))

