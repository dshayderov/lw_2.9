#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit

no_intr_fact = '''
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
'''

no_intr_fib = '''
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
'''

intr_fact = '''
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
@tail_call_optimized
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
'''

intr_fib = '''
class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        while f and f.f_code.co_filename == f:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
@tail_call_optimized
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)
'''

if __name__ == '__main__':
    print('Результат факториала:', timeit.timeit(setup=no_intr_fact, number=1000))
    print('Результат числа Фибоначи:', timeit.timeit(setup=no_intr_fib, number=1000))
    print('Результат факториала с интроспекцией стека:', timeit.timeit(setup=intr_fact, number=1000))
    print('Результат числа Фибоначи с интроспекцией стека:', timeit.timeit(setup=intr_fib, number=1000))