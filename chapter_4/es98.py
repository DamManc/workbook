# Exercise 98: Is a Number Prime?
def is_prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif (n / 2).is_integer() or (n / 3).is_integer() or (n / 5).is_integer() or (n / 7).is_integer():
        return False
    else:
        return True


def main():
    n = int(input("Enter a integer: "))
    while n <= 0:
        n = int(input("Enter a affective integer > 0: "))
    if is_prime(n):
        print(f'{n} is a prime number')
    else:
        print(f'{n} is Not a prime number')


if __name__ == '__main__':
    main()