def main():
    print('Enter a number (blank to finish) and press enter to continue')
    in_usr = input()
    sum = 0
    while in_usr:
        try:
            n_usr = float(in_usr)
            sum += n_usr
            print(f'the current sum is {sum}')
            in_usr = input()
        except ValueError:
            print('Enter a valid number, blank to finish')
            in_usr = input()


if __name__ == '__main__':
    main()
