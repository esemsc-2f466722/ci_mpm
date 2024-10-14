
__all__ = ['my_sum', "factorial"]

from functools import cache


@cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot
