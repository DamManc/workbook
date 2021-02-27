# MultipleWord Palindromes
str = input("Enter a string: ")
str_n = str.replace(" ", "")
initial = 0
last = len(str_n) - 1
value = 0

for ch in str_n:
    if ch == str_n[last]:
        last -= 1
        value = 1
    else:
        value = 0

if value == 0:
    print("Your string is NOT Palindrome")
else:
    print("Your string is a Palindrome")
