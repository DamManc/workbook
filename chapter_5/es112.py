# Exercise 112:Remove Outliers
from es110 import sort_n


def rem_n(new_n, d):
    f_n = sorted(new_n[:])
    lar_st = len(f_n) - d
    smal_end = 0 + d
    return f_n[smal_end:lar_st]


def main():
    n = input('Enter integers (0 to finish and move forward): ')
    while not n.isnumeric():
        print('Enter a valid integer pls..')
        n = input('Enter integers (0 to finish and move forward): ')
    new_n = sort_n(n)
    while not len(new_n) > 3:
        print('You should enter at least 4 integers pls..')
        n = input('Enter integers (0 to finish and move forward): ')
        new_n.append(int(n))
    print('''Enter a number N
    Caution! 2 * N number will be deleted (N largest and N smallest)..''')
    d = input()
    while not d.isnumeric() and d != '0':
        print('Enter a valid integer pls ( > 0)..')
        d = input()
    last_seq = rem_n(new_n, int(d))
    print(f'The sequence entered: {new_n}')
    print(f'The New sequence: {last_seq}')


if __name__ == '__main__':
    main()
