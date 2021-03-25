# Exercise 109: Magic Dates
from es106 import days_in_month

YEARS = 100
CENTURY = 1900
MONTHS = 12


def det_magic():
    magic_year = []
    for y in range(1, YEARS + 1):
        year = CENTURY + y
        for m in range(1, MONTHS + 1):
            month = m
            for d in range(1, days_in_month(m, year) + 1):
                if d * m == y:
                    magic_year.append(f"day: {d}th ___ month: {m}th ___ year: {year}")
    return magic_year


def main():
    years = det_magic()
    print('All magic dates are: ')
    for i in years:
        print(i)


if __name__ == '__main__':
    main()
