def foo(n):
    if (num := n**2) >= 100:
        return num
    return f'{n}^2 < 100'


print(foo(10))
