# Prime Factors
n = int(input("Enter an integer (2 or greater): "))
div_prime = []
factor = 2
while factor <= n:
    if n % factor == 0:
        div_prime.append(factor)
        n = n // factor
    else:
        factor += 1
print(div_prime)
