# Exercise 113:Avoiding Duplicates

def av_dup(words):
    i = 0
    while i < len(words):
        if words[i] in words[i+1:]:
            del words[i]
        i += 1
    return words


def main():
    i = input('Enter a string (blank line to finish): ')
    words = []
    while not i == '':
        words.append(i.strip())
        i = input('Enter a string (blank line to finish): ')
    print(f'Sequence entered: {words}')
    print(f'Sequence without duplicate: {av_dup(words)}')


if __name__ == '__main__':
    main()
