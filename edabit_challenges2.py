def factor_odd_or_even(num):
    return 'odd' if (num ** 0.5)%1 == 0 else 'even'

print(factor_odd_or_even(101))