# Exercise 108: Reduce Measures
TABLESPOON = 3
CUP = 48
TEASPOONS = 1


def red_meas(n, u):
    if u == 'c':
        n = n * CUP
    elif u == 'table':
        n = n * TABLESPOON
    n_init = n
    cup = n // CUP
    n = n - cup * CUP
    table = n // TABLESPOON
    n = n - table * TABLESPOON
    tea = n
    return cup, table, tea


def main():
    n_units = input('Enter a number of units as integer ( > 0): ')
    while not n_units.isnumeric() or int(n_units) == 0:
        print('your input is not a correct value: ')
        n_units = input('Enter a number of units as integer ( > 0): ')
    unit_of = input('Enter a unit of measure (table as tablespoon, c as cup, tea as teaspoons): ')
    while unit_of != 'table' and unit_of != 'c' and unit_of != 'tea':
        print('your input is not a correct value: ')
        unit_of = input('Enter a unit of measure (table as tablespoon, c as cup, tea as teaspoons): ')
    red_value = red_meas(int(n_units), unit_of)
    print(f'Your Measure reduces are: {red_value[0]} cup, {red_value[1]} tablespoon, {red_value[2]} teaspoon')


if __name__ == '__main__':
    main()
