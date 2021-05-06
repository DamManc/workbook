LIMIT_APPR = 10 ** -12

def square_root(n, guess=1.0):
    # base case
    if n <= guess ** 2 < n + LIMIT_APPR:
        return guess
    else:
        second_param = (guess + (n / guess)) / 2
        return square_root(n, second_param)

def main():
    n = input('Enter a number to calculate its square root: ')
    if not n:
        print('You have not entered a value..')
    else:
        try:
            n = float(n)
            print(square_root(n))
        except ValueError:
            print('You have not entered a number..')
            quit()


if __name__ == '__main__':
    main()