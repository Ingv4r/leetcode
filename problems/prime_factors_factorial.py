from decimal import Decimal

class Answer:

    @staticmethod
    def fact(n):
        factorial = 1
        while n > 0:
            factorial = factorial * n
            n -= 1
        return factorial

    def decomp(self, n):
        factorial = self.fact(n)
        res = ''
        primfac = []
        i = 2
        degree = 0
        while i * i <= factorial:
            while factorial % i == 0:
                degree += 1
                factorial = factorial / i
            if degree >= 2:
                res += f'{i}^{degree} * '
                degree = 0
            elif degree == 1:
                res += f'{i} * '
                degree = 0
            i = i + 1
        if factorial > 1:
            res += f'{int(factorial)}'

        return res, self.fact(n), 2**82*17*1399*89847576677


n = 35
print(Answer().decomp(n), )