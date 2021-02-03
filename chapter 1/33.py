#Body Sort 3 Integers
print('Sort 3 Integers')
n_1 = int(input("Enter the first integer: "))
n_2 = int(input("Enter the second integer: "))
n_3 = int(input("Enter the third integer: "))
min = min(n_1, n_2, n_3)
max = max(n_1, n_2, n_3)
mid = (n_3 + n_2 + n_1) - min - max
print("Sorted: %i, %i, %i" %(min, mid, max))