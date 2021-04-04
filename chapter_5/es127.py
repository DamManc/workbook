# Exercise 127: Is a List already in Sorted Order?


def is_sorted(numbers):
    if len(numbers) > 1:
        if numbers[0] > numbers[1]:
            for i in range(1, len(numbers)):
                if numbers[i-1] > numbers[i]:
                    v = True
                else:
                    v = False
        else:
            for i in range(1, len(numbers)):
                if numbers[i-1] < numbers[i]:
                    v = True
                else:
                    v = False
        return v
    else:
        return 'Your list have only one element..'


def main():
    numbers = []
    i = input('Enter a number (blank to finish): ')
    while i != '':
        try:
            n = float(i)
            numbers.append(n)
            i = input('Enter a number (blank to finish): ')
        except ValueError:
            i = input('Enter a number (blank to finish): ')
    print(numbers)
    print(f'Is a List already in Sorted Order? {is_sorted(numbers)}')


if __name__ == '__main__':
    main()
