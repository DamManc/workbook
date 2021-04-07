# Exercise 96: Does a String Represent an Integer?


def is_integer(a):
    new_int = a.strip()
    if ((a[0] == '+' or a[0] == '-') and a[1:].isdigit()) or a.isdigit():
        return True
    else:
        return False


def main():
    int = input('Enter a integer: ')
    if is_integer(int):
        print('Your input is a valid integer!')
    else:
        print('Your input is not a integer!')


if __name__ == '__main__':
    main()
