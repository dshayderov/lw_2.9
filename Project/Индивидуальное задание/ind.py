# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_min(li):
    if len(li) == 2:
        if li[1] < li[0]:
            return li[1]
        else:
            return li[0]
    else:
        minim = list_min(li[1:])
        if li[0] < minim:
            return li[0]
        else:
            return minim


if __name__ == '__main__':
    sp = list(map(float, input("Введите список чисел: ").split(' ')))
    c = list_min(sp)
    print(f"Минимальный элемент списка: {c}")