# Exercise 135:The Sieve of Eratosthenes


def find_prime(n1, n2):
    primes = []
    for i in range(n1, n2):
        primes.append(i)
    primes[1] = 0
    for n in primes:
        if n == 0:
            continue
        else:
            p = n
            while p < n2:
                if p != n:
                    primes[p] = 0
                p += n
    new_primes = []
    for prime in primes:
        if prime != 0:
            new_primes.append(prime)
    return new_primes


def main():
    limit = int(input('Enter a number as limit of primes numbers to visualize: '))
    print(find_prime(0, limit))


if __name__ == '__main__':
    main()