# Exercise 116: Perfect Numbers
from es115 import calc_div


def is_magic(x):
    if sum(calc_div(x)) == x:
        return True
    else:
        return False


def calc_magic(x):
    str_res = []
    for i in calc_div(x):
        str_res.append(str(i))
    return str_res


def main():
    n = input('Enter a number: ')
    try:
        x = int(n)
        if x <= 10_000:
            if is_magic(x):
                print('Your number is Perfect!')
                print(f'{x} is equal to {"+".join(calc_magic(x))}')
            else:
                print('Your number is not Perfect, Sorry :( ')
        else:
            print('Your entered number is too big, sorry')
            main()
    except ValueError:
        print('Enter a valid number..')
        main()


if __name__ == '__main__':
    main()
