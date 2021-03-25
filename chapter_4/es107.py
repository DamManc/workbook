# Exercise 107: Reduce a Fraction to Lowest Terms
from chapter_3 import es79


def red_fra(n, d):
    greatest_divisor = es79.greatest_divisor(n, d)
    new_num = n // greatest_divisor
    new_den = d // greatest_divisor
    return new_num, new_den


def main():
    num = input('Enter a number (numerator): ')
    denom = input('Enter a number (denominator): ')

    while not num.isnumeric() or not denom.isnumeric():
        num = input('Enter a number (numerator): ')
        denom = input('Enter a number (denominator): ')

    print(f'The reduced fraction: {red_fra(int(num), int(denom))[0]} / {red_fra(int(num), int(denom))[1]}')


if __name__ == '__main__':
    main()
