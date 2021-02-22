# Approximate π
n1 = 3
count = 1
while count <= 15:
    n2 = n1 + 1
    n3 = n2 + 1
    if count == 1:
        initial = 3
    elif count % 2 == 0:
        initial += 4 / (n1 * n2 * n3)
    else:
        initial -= 4 / (n1 * n2 * n3)
    print(initial)
    count += 1
    n1 = n3
