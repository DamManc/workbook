# Exercise 103: Random Good Password
from es100 import gen
from es102 import is_good


def main():
    count = 0
    while not is_good(gen()):
        count += 1
    print(f'Number of attempts before the password was correct: {count}')
    print(gen())


if __name__ == '__main__':
    main()
