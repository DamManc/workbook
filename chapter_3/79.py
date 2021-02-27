# Greatest Common Divisor
m = int(input("Enter an integer: "))
n = int(input("Enter a second integer: "))
if m < n:
    d = m
else:
    d = n
while d % m != 0 or d % n != 0:
    d -= 1
print("The greatest common divisor of %d and %d is %d" % (m, n, d))
