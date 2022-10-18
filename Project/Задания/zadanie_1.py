#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


fact_rec = '''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


fib_rec = '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


fact_itr = '''
def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product
'''


fib_itr = '''
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
'''


fact_lru = '''
from functools import lru_cache
@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


fib_lru = '''
from functools import lru_cache
@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


if __name__ == '__main__':
    print('Рекурсивный факториал:', timeit.timeit(setup=fact_rec, number=1000))
    print('Рекурсивное число Фибоначи:', timeit.timeit(setup=fib_rec, number=1000))
    print('Итеративный факториал:', timeit.timeit(setup=fact_itr, number=1000))
    print('Итеративное число Фибоначи:', timeit.timeit(setup=fib_itr, number=1000))
    print('Факториал с декоратором:', timeit.timeit(setup=fact_lru, number=1000))
    print('Число Фибоначи с декоратором:', timeit.timeit(setup=fib_lru, number=1000))