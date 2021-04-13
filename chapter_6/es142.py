# Exercise 142: Unique Characters
def unique_ch(s):
    table = {}
    for ch in s:
        if ch not in table:
            table[ch] = 1
        else:
            table[ch] += 1

    return len(table)


def main():
    print('Enter a string')
    usr_input = input()
    print(f'The number of unique characters is {unique_ch(usr_input)}')


if __name__ == '__main__':
    main()
