# Exercise 100: Random Password
import random
POS_ASCII_START = 36
POS_ASCII_END = 126
RANDOM_LENGTH_MIN = 7
RANDOM_LENGTH_MAX = 10


def print_pw():
    print(gen())


def gen():
    pw = ''
    for i in range(0, random.randint(RANDOM_LENGTH_MIN, RANDOM_LENGTH_MAX)):
        pw += chr(random.randint(POS_ASCII_START, POS_ASCII_END))
    return pw


if __name__ == '__main__':
    print_pw()