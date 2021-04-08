# Exercise 135:The Sieve of Eratosthenes
import threading
import time
import random


def find_prime(name, n1, n2):
    print(f'{name} starts ---> {n2} as limit (not included)')
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
    new_primes.append(f'{name} has finished')
    time.sleep(1)
    print(new_primes)


def threads():
    init = 0
    start = time.time()
    threads = []
    for i in range(5):
        limit = random.randrange(5, 100)
        #limit = 10000
        name = f'Tread{i}'
        t = threading.Thread(target=find_prime, args=(name, init, limit))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    finish = time.time()
    print(f'Elapsed time {round(finish - start, 2)}')


if __name__ == '__main__':
    threads()
