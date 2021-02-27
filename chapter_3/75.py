# Is a String a Palindrome?
str = input("Enter a string: ")
initial = 0
last = len(str) - 1
value = 0

for ch in str:
    if ch == str[last]:
        last -= 1
        value = 1
    else:
        value = 0

if value == 0:
    print("Your string is NOT Palindrome")
else:
    print("Your string is a Palindrome")
