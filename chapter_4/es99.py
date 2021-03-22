# Exercise 99: Next Prime
from es98 import is_prime


def next_prime(n):
    while True:
        n = n + 1
        if is_prime(n):
            return n


def main():
    n = int(input('Enter a integer: '))
    while n <= 0:
        n = int(input('Enter a valid integer > 0: '))
    print(f'{next_prime(n)} is the greatest prime number after {n}')


if __name__ == '__main__':
    main()
