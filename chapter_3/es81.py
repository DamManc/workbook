# Binary to Decimal

def bi_to_dec(b, base=2):
    decimal_number = 0
    len_n = len(b) - 1
    for i in b:
        cf = int(i)
        decimal_number += cf * (base ** len_n)
        len_n -= 1
    return decimal_number


def main():
    binary_number = input("Enter a binary number: ")
    while not binary_number.isdigit():
        print('Your number is not valid')
        binary_number = input("Enter a binary number: ")
    decimal_number = bi_to_dec(binary_number)
    print(f"The equivalent decimal number is {decimal_number}")


if __name__ == '__main__':
    main()
