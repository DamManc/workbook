# Word by Word Palindromes
from es117 import get_words


def calc_pal(l_str):
    check = False
    for i in range(0, len(l_str)):
        if l_str[i] == l_str[-(i + 1)]:
            check = True
        else:
            check = False
    return check


def main():
    s = input('Enter a string: ')
    if calc_pal(get_words(s.strip())):
        print('You have entered a Word by Word Palindrome!')
    else:
        print('Your input is not a Word by Word Palindrome, sorry..')


if __name__ == '__main__':
    main()
