# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def recursion(n):
    if n == 1:
        return 1

    return n + recursion(n - 1)


if __name__ == '__main__':
    x = int(input("Введите число: "))
    print(recursion(x))