import sys


def main():
    if len(sys.argv) != 2:
        print('You must write the name of a file to open')
        quit()
    try:
        fin = open(sys.argv[1], 'r')
        line = fin.readline()
        histo = {}
        while line:
            for word in line.split():
                if word not in histo:
                    histo[word] = len(word)
            line = fin.readline()
        list_words = []
        for word, l in histo.items():
            list_words += [(l, word)]
        list_words.sort(reverse=True)
        max_v = list_words[0][0]
        longest_w = [value for value in list_words if value[0] == max_v]
        print(f'The longest word/words is/are {longest_w}')
        print(f'Words of that length that occurred in the file {histo}')
        fin.close()
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
