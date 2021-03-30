# Exercise 122: Pig Latin
import string


def cons_low():
    cons_low = ''
    for ch in string.ascii_lowercase:
        if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u':
            cons_low += ch
    return cons_low


def eng_to_pig(s):
    words = s.split()
    new_words = []
    for word in words:
        if word[0] in cons_low():
            i = 0
            while word[i] in cons_low():
                new_word = word[i + 1:]
                new_word += word[i]
                i += 1
            new_word += 'ay'
        else:
            new_word = word[:]
            new_word += 'way'
        new_words.append(new_word)
    return new_words


def main():
    print('Enter a string in english to translate in Pig Latin:')
    s = input()
    print('Your string in Pig Latin:')
    print(' '.join(eng_to_pig(s.strip())))


if __name__ == '__main__':
    main()
