# Multiplication Table
first = 0
last = 10
index = 1
number = 1
first_row = 1
print(" ", " ", end="")
for int in range(first, last):
    print(first_row, " ", end="")
    first_row += 1
print()
for int in range(first, last):
    for int in range(first, last + 1):
        if int <= 1:
            print(number, " ", end="")
        else:
            index += 1
            print(number * index, " ", end="")
    print()
    number += 1
    index = 1
