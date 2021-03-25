# Exercise 104: Hexadecimal and Decimal Digits


def hex_to_dec(str_hex, base=16):
    e = len(str_hex) - 1
    str_int = 0
    for ch in str_hex.upper():
        if ch == 'A':
            int_v = 10
        elif ch == 'B':
            int_v = 11
        elif ch == 'C':
            int_v = 12
        elif ch == 'D':
            int_v = 13
        elif ch == 'E':
            int_v = 14
        elif ch == 'F':
            int_v = 15
        else:
            int_v = int(ch)
        str_int += int_v * (base ** e)
        e -= 1
    return str_int


def dec_to_hex(v_int):
    str_hex = ''
    while True:
        quo = v_int // 16
        rest = v_int % 16
        if rest == 15:
            hex_v = 'F'
        elif rest == 14:
            hex_v = 'E'
        elif rest == 13:
            hex_v = 'D'
        elif rest == 12:
            hex_v = 'C'
        elif rest == 11:
            hex_v = 'B'
        elif rest == 10:
            hex_v = 'A'
        else:
            hex_v = str(rest)
        str_hex += hex_v
        str_hex_rev = str_hex[::-1]
        v_int = quo
        if v_int == 0:
            return str_hex_rev


def print_result():
    init_str = input('What number conversion are you doing, for hex to int digit int, for int to hex digit hex: ')
    while not (init_str == 'int' or init_str == 'hex'):
        init_str = input('For hex to int digit int, for int to hex digit hex: ')
    init_n = input('Enter the entity to convert: ')
    if init_str == 'int':
        result_str = hex_to_dec(init_n)
    else:
        result_str = dec_to_hex(int(init_n))
    print(f'Your result is {result_str}')


if __name__ == '__main__':
    print_result()
