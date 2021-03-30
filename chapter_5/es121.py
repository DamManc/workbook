# Exercise 121: Random Lottery Numbers

import random


def draw(n=0):
    drawn_ns = []
    for i in range(0, n):
        d = random.randint(0, 49)
        drawn_ns.append(d)
    return drawn_ns


def main():
    numbers = draw(6)
    print(str(sorted(numbers))[1:-1])


if __name__ == '__main__':
    main()
