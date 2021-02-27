# Decimal to Binary
decimal_number = int(input("Enter a decimal number: "))
binary_number = ""
while decimal_number != 0:
    div = decimal_number // 2
    rem = decimal_number % 2
    binary_number += str(rem)
    decimal_number = div

print("The equivalent binary number is %s" % binary_number[::-1])
