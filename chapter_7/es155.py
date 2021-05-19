import re
import sys
sys.path.append('/home/dam/code/py/workbook/chapter_5')
from es117 import rem_punt


def main():
    if len(sys.argv) != 2:
        print('You must write the name of a file to open')
        quit()
    try:
        fin = open(sys.argv[1], "r")
        line = fin.readline()
        histo = {}
        while line:
            list_words_line = rem_punt(line.lower())
            for word in list_words_line:
                if word not in histo:
                    histo[word] = 1
                else:
                    histo[word] += 1
            line = fin.readline()
        print(histo)
        fin.close()
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
