# Exercise 102: Check a Password

def is_good(pw):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    if 8 > len(pw) or len(pw) > 22:
        return False
    for ch in pw:
        if ch.islower():
            count_lower += 1
        elif ch.isupper():
            count_upper += 1
        elif ch.isdigit():
            count_digit += 1
    if count_lower > 0 and count_digit > 0 and count_upper > 0:
        return True
    else:
        return False


def main():
    pw = input('Enter a password (8 < pw < 22) with at least one uppercase, one lowercase letter and one number: ')
    if is_good(pw):
        print('The entered password is correct!!')
    else:
        print('The entered password is not correct')
        main()


if __name__ == '__main__':
    main()
