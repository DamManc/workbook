# Exercise 123: Pig Latin Improved
import string
from es122 import cons_low


def cons():
    c = ''
    for ch in string.ascii_letters:
        if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != 'A' and ch != 'E' and ch != 'I' \
                and ch != 'O' and ch != 'U':
            c += ch
    return c


def eng_to_pig(s):
    words = s.split()
    new_words = []
    for word in words:
        pun = 0
        if word[-1] == '!':
            word = word[:-1]
            pun = 1
        if word[0] in cons():
            i = 0
            while word[i] in cons():
                if word[i] not in cons_low():
                    new_word = word[i + 1:].capitalize()
                    new_word += word[i].lower()
                else:
                    new_word = word[i + 1:]
                    new_word += word[i]
                i += 1
            new_word += 'ay'
        else:
            new_word = word[:]
            new_word += 'way'
        if pun == 1:
            new_word += '!'
        new_words.append(new_word)
    return new_words


def main():
    print('Enter a string in english to translate in Pig Latin:')
    s = input()
    print('Your string in Pig Latin:')
    print(' '.join(eng_to_pig(s.strip())))


if __name__ == '__main__':
    main()
