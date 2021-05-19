# Exercise 117: Only the Words
import re


def rem_punt(in_str):
    list_word = in_str.split()
    for i in range(len(list_word)):
        list_word[i] = re.sub('[^A-Za-z]$','',list_word[i])
    return list_word


def main():
    in_str = input('Enter a string: ')
    print(f'Your new string without punctuation marks is {rem_punt(in_str)}')


if __name__ == '__main__':
    main()
