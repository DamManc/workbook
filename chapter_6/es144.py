# Exercise 144: Anagrams Again

def anagrams(s1, s2):
    table_one = {}
    table_two = {}
    for ch in s1.replace(' ', '').upper():
        if ch not in table_one:
            table_one[ch] = 1
        else:
            table_one[ch] += 1
    for ch in s2.replace(' ', '').upper():
        if ch not in table_two:
            table_two[ch] = 1
        else:
            table_two[ch] += 1
    if table_one == table_two:
        return True
    else:
        return False


def main():
    print('Enter a string')
    usr_input_one = input()
    print('Enter a second string')
    usr_input_two = input()
    if anagrams(usr_input_one, usr_input_two):
        print('This two word are anagrams')
    else:
        print('This two word are not anagrams')


if __name__ == '__main__':
    main()