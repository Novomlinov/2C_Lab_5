# Даны долги клиентов банка. Найти максимальный долг
# и суммарный долг, больший 40000.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def duty(*args):
    if args:
        summa = 0

        values = [int(arg) for arg in args]

        for idx in values:
            if idx >= 40000:
                summa += idx
        print(f"Суммарный долг, больший 40000: {summa}. Максимальный долг: {idx}")
    else:
        return None


if __name__ == "__main__":
    duty(20150, 22150, 45224, 46000)
    duty(40000, 30000, 10000, 0)
    duty(300, 600, 550, 800)
    duty(1240, 1000, 3000, 9000)
    duty(40000, 80000, 100000, 120000)
    duty(3000, 6000, 5500, 8000)