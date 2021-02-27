# Square Root
number = float(input("Enter a number: "))
guess = number / 2
absolute_value = abs((guess * guess) - number)
LIMIT_APPR = 10 ** -12

while absolute_value > LIMIT_APPR:
    guess = (guess + number / guess) * 0.5
    absolute_value = abs((guess * guess) - number)

print("an approximation of the square root is ", guess)
