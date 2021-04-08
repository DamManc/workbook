# Exercise 136: Reverse Lookup
import random
import string


def reverse_lookup(d, v):
    reverse = {}
    for k in d:
        value = d[k]
        if value not in reverse:
            reverse[value] = [k]
        else:
            reverse[value].append(k)
    try:
        result = reverse[int(v)]
    except KeyError:
        result = []
    return result


def main():
    d = {}
    for i in range(20):
        d[string.ascii_uppercase[random.randrange(26)]] = random.randrange(10)
    print(f"You have this dictionary {d}")
    print("Enter a value to search and display all keys related with that value")
    v = input()
    print(reverse_lookup(d, v))


if __name__ == '__main__':
    main()
