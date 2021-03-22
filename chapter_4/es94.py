# Exercise 94: Is It a Valid Triangle?


def is_no_zero(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return True
    else:
        return False


def is_valid_tr(a, b, c):
    if a > (b + c) or b > (a + c) or c > (a + b):
        return False
    else:
        return True


def main():
    first_length = int(input("Enter the first length straw: "))
    second_length = int(input("Enter the second length straw: "))
    third_length = int(input("Enter the third length straw: "))
    if is_no_zero(first_length, second_length, third_length):
        if is_valid_tr(first_length, second_length, third_length):
            print('Yes, can be used to form a triangle')
        else:
            print('No, cannot be used to form a triangle')
    else:
        print('Your lengths are not valid...')
        main()


if __name__ == '__main__':
    main()
