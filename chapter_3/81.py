# Binary to Decimal
binary_number = input("Enter a binary number: ")
decimal_number = 0
len_n = len(binary_number) - 1
for i in binary_number:
    cf = int(i)
    decimal_number += cf * (2 ** len_n)
    len_n -= 1
print("The equivalent decimal number is %d" % decimal_number)
