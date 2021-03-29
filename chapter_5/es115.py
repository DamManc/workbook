# Exercise 115: List of Proper Divisors


def calc_div(n):
    div = []
    factor = 1
    while factor < n:
        if n % factor == 0:
            div.append(factor)
        factor += 1
    return div


def main():
    n = input('Enter a number: ')
    try:
        x = int(n)
        div = calc_div(x)
    except ValueError:
        print('enter a valid number')
        main()
    print(f'List of Proper Divisors: {div}')


if __name__ == '__main__':
    main()
