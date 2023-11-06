from time import sleep


def cash(func):
    def wrapper(*args, **kwargs):
        cash_key = args + tuple(kwargs.items())
        if cash_key not in cash_dict:
            cash_dict[cash_key] = func(*args, **kwargs)
        return cash_dict[cash_key]
    cash_dict = {}
    return wrapper


@cash
def func(n):
    sleep(1)
    return n**2


def fib_ger(second=0, first=1):
    yield second + first
    second, first = first, second + first



print(list(fib_ger()))
print(list(fib_ger()))
print(list(fib_ger()))
print(list(fib_ger()))
