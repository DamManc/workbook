# Exercise 143: Anagrams
def anagrams(s1, s2):
    table_one = {}
    table_two = {}
    for ch in s1:
        if ch not in table_one:
            table_one[ch] = 1
        else:
            table_one[ch] += 1
    for ch in s2:
        if ch not in table_two:
            table_two[ch] = 1
        else:
            table_two[ch] += 1
    if table_one == table_two:
        return True
    else:
        return False


def main():
    print('Enter a word')
    usr_input_one = input()
    while len(usr_input_one.split()) > 1:
        print('No more than one word, enter a new word')
        usr_input_one = input()
    print('Enter a second word')
    usr_input_two = input()
    while len(usr_input_two.split()) > 1:
        print('No more than one word, enter a new word')
        usr_input_two = input()
    if anagrams(usr_input_one, usr_input_two):
        print('This two word are anagrams')
    else:
        print('This two word are not anagrams')


if __name__ == '__main__':
    main()