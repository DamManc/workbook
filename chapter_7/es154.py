import sys
import re


def main():
    if len(sys.argv) != 2:
        print('You must write the name of a file to open')
        quit()
    try:
        fin = open(sys.argv[1], "r")
        line = fin.readline()
        histo = {}
        while line:
            n_line = re.sub('[^A-Za-z]', '', line.lower())
            for ch in n_line:
                if ch not in histo:
                    histo[ch] = 1
                else:
                    histo[ch] += 1
            line = fin.readline()
        print(histo)
        fin.close()
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
