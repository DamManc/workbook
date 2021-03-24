# Decimal to Binary

def dec_to_bi(d, base=2):
    binary_number = ''
    while d != 0:
        div = d // base
        rem = d % base
        binary_number += str(rem)
        d = div
    return binary_number[::-1]


def main():
    decimal_number = int(input("Enter a decimal number: "))
    b = dec_to_bi(decimal_number)
    print(f"The equivalent binary number is {b}")


if __name__ == '__main__':
    main()
