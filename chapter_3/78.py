# The Collatz Conjecture
n = int(input("Enter a integer: "))
while n > 0:
    while n != 1:
        print(n, "->", end="")
        if n % 2 == 0:
            another_term = n // 2
            n = another_term
        else:
            another_term = (n * 3) + 1
            n = another_term
    print(" Finished..")
    n = float(input("Enter a new integer: "))
