# Exercise 117: Only the Words
import re

def get_words(words):
    for word in words.split():
        new = re.sub('[*?!,":;.\'/', )


def main():
    words = input('Enter a string: ')
    print(f'Your new string without punctuation marks is [{" ".join(get_words(s))}]')


if __name__ == '__main__':
    main()
