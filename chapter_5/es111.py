# Exercise 111: Reverse Order
def sort_n_rev(n, t_n=[]):
    while n != "0":
        t_n.append(int(n))
        n = input('Enter integers (0 to finish): ')
        if not n.isnumeric():
            print('Enter a valid integer pls..')
            n = input('Enter integers (0 to finish and sort): ')
    return sorted(t_n, reverse=True)


def main():
    n = input('Enter integers (0 to finish and sort): ')
    while not n.isnumeric():
        print('Enter a valid integer pls..')
        n = input('Enter integers (0 to finish and sort): ')
    for v in sort_n_rev(n):
        print(v)


if __name__ == '__main__':
    main()