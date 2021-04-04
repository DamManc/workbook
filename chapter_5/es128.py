# Exercise 128: Count the Elements


def count_range(numbers, min, max):
    c = 0
    for i in range(0, len(numbers)):
        if min <= numbers[i] < max:
            c += 1
    return c


def main():
    numbers = []
    i = input('Enter a number (blank to finish and move forward..): ')
    while i != '':
        try:
            n = float(i)
            numbers.append(n)
            i = input('Enter a number (blank to finish and move forward..): ')
        except ValueError:
            i = input('Enter a number (blank to finish and move forward..): ')
    f = 0
    while f != 1:
        i_min = input('Enter a Number as a minimum (blank to use the minimum list numbers): ')
        if i_min != '':
            try:
                min = float(i_min)
                f = 1
            except ValueError:
                print('Your entered input is not a numbers..')
        else:
            min = min(numbers)
            f = 1
    g = 0
    while g != 1:
        i_max = input('Enter a Number as a maximum (blank to use the maximum list numbers): ')
        if i_max != '':
            try:
                max = float(i_max)
                g = 1
            except ValueError:
                print('Your entered input is not a numbers..')
        else:
            max = max(numbers)
            g = 1
    print(
        f'The number of element within the list that are greater than or equal to some minimum value and less than '
        f'some maximum value: {count_range(numbers, min, max)}')


if __name__ == '__main__':
    main()
