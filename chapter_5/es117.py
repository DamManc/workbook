# Exercise 117: Only the Words


def get_words(s):
    old_words = s.rsplit()
    new_words = []
    pun_marks = ['?', '.', ',', '\'', ':', ';', '!', '-']
    for w in old_words:
        if w[-1] in pun_marks:
            for p in pun_marks:
                if w[-1] == p:
                    new_words.append(w.removesuffix(p))
        else:
            new_words.append(w)
    return new_words


def main():
    s = input('Enter a string: ')
    print(f'Your new string without punctuation marks is \'{" ".join(get_words(s))}\'')


if __name__ == '__main__':
    main()
