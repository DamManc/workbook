# Exercise 119: Below and Above Average


def avg(numbers):
    s = sum(numbers)
    return s / len(numbers)


def main():
    x = input('Enter some numbers (blank): ')
    numbers = []
    while x != '':
        try:
            n = int(x)
            numbers.append(n)
            x = input('Enter some numbers (blank): ')
        except ValueError:
            print('Enter a valid input..')
            x = input('Enter some numbers (blank): ')
    print(f'The AVG is {round(avg(numbers), 2)}')
    numbers.append(round(avg(numbers), 2))
    print(f'Numbers: {sorted(numbers)}')


if __name__ == '__main__':
    main()
