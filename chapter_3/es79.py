# Greatest Common Divisor

def greatest_divisor(m, n):
    d = 0
    if m < n:
        d = m
    else:
        d = n
    while not m % d == 0 or not n % d == 0:
        d -= 1
    return d


def main():
    n_one = int(input("Enter an integer: "))
    n_two = int(input("Enter a second integer: "))
    print(f"The greatest common divisor of {n_one} and {n_two} is {greatest_divisor(n_one, n_two)}" )


if __name__ == '__main__':
    main()