# Exercise 106: Days in a Month
from chapter_2.es58 import check_leap


def days_in_month(month, year):
    if check_leap(year) and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month == 1:
        return 31
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31


def main():
    m = input('Enter a number of one month (1-12): ')
    while not m.isnumeric() or int(m) > 12 or int(m) == 0:
        print('Your input is not correct')
        m = input('Enter a number of one month (1-12): ')
    y = input('Enter a number of one year: ')
    while not m.isnumeric():
        print('Your input is not a number')
        y = input('Enter a number of one month (1-12):')
    print(f'In the {m}th month there are {days_in_month(int(m), int(y))} days')


if __name__ == '__main__':
    main()

