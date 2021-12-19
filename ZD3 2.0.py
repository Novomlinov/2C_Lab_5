# Даны долги клиента банка.
# Вывести долги за последние месяцы.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_debts(debtor, **kwargs):
    print(f"Names of debtors: {debtor}")
    for kwarg, debts in kwargs.items():
        print(f"{kwarg}: {debts}")


if __name__ == "__main__":
    print_debts(
        "Lebowski",
        January="250.000$", February="200.000$",
        March="400.000$", April="150.000$"
    )