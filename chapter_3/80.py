# Prime Factors
n = int(input("Enter an integer (2 or greater): "))
factor = 2
while factor < n:
    if n % factor == 0:
        n = n // factor
    else:
        factor += 1
    print(factor)