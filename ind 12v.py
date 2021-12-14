#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def summ(*args):
    if args:
        summa = 0

        values = [int(arg) for arg in args]
        max_idx = max(args)

        for idx in values:
            if idx < max_idx:
                summa += idx
            if idx >= max_idx:
                return summa
    else:
        return None


if __name__ == "__main__":
    print(summ(3, -8, 3, -5, -7))
    print(summ(-1, 3, 8, -4, 3, -9))
    print(summ(3, 6, -5, 8, 7, -4))
    print(summ(124, -6, 235, 8, 7, -100, 15, -15, 25, -52))