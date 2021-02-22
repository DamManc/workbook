# Fizz-Buzz
print("The firts 100 numbers in the Fizz-Buzz game")
count = 1
first = 1
while count <= 100:
    if (count % 3 == 0) and (count % 5 == 0):
        print("Buzz and Frizz")
    elif count % 3 == 0:
        print("Frizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1