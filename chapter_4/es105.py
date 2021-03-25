# Exercise 105: Arbitrary Base Conversions
from es104 import *
from chapter_3.es81 import bi_to_dec
from chapter_3.es82 import dec_to_bi


def check_input_n(n, base):
    count = 0
    for ch in n.upper():
        if int(base) > 10:
            try:
                n_ch = int(ch)
                if n_ch > int(base):
                    count += 1
            except ValueError:
                if ch > 'F' or (ch == 'A' and int(base) < 11) or (ch == 'B' and int(base) < 12) or (
                        ch == 'C' and int(base) < 13) \
                        or (ch == 'D' and int(base) < 14) or (ch == 'E' and int(base) < 15) or (
                        ch == 'F' and int(base) < 16):
                    count += 1
        if int(base) < 10 and int(ch) >= int(base):
            count += 1
    if count == 0:
        return True
    else:
        return False


def main():
    base_old = input('Enter a base (2-16): ')

    while not base_old.isdigit() or int(base_old) < 2 or int(base_old) > 16:
        print('Enter a valid base..')
        base_old = input('Enter a base (2-16): ')

    n = input('Enter a number in that base: ')

    while not check_input_n(n, base_old):
        print('Your number is not correct for that base..')
        n = input('Enter a number in that base: ')

    if int(base_old) > 10:
        res_de = hex_to_dec(n, int(base_old))
    else:
        res_de = bi_to_dec(n, int(base_old))

    base_new = input('Enter a new base (2-16): ')

    while not base_new.isdigit() or int(base_new) < 2 or int(base_new) > 16:
        print('Enter a valid base..')
        base_new = input('Enter a base (2-16): ')

    if base_new == '10':
        print(f'Your number in {base_new} is: {res_de}')
    else:
        if int(base_new) > 10:
            res_final = dec_to_hex(int(res_de), int(base_new))
        else:
            res_final = dec_to_bi(int(res_de), int(base_new))

    print(f'Your number in {base_new} is: {res_final}')


if __name__ == '__main__':
    main()
