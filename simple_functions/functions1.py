
__all__ = ['my_sum', "factorial", "my_sin"]

from functools import cache


@cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


def my_sin(iterable):
    res = 0
    pow = iterable
    fact = 1
    for i in range(10):
        res += pow / fact
        pow *= -1 * iterable ** 2
        fact *= (2*(i+1))*(2*(i+1)+1)
    return res
