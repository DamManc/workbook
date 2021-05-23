import sys
import re


def main():
    if len(sys.argv) != 2:
        print('You must insert the file to read..')
        quit()
    try:
        fin = open(sys.argv[1], 'r')
        counts = {}
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            counts[ch] = 0
        unique = []
        num_words = 0
        for line in fin:
            for ch in line.strip().upper():
                if ch.upper() in counts.keys():
                    unique.append(ch.upper())
            num_words += 1
        for ch in unique:
            counts[ch] += 1
        fin.close()
        smallest = min(counts.values())
        for ch in counts:
            if counts[ch] == smallest:
                smallest_letter = ch
            percentage = counts[ch] / num_words * 100
            print(ch, "occurs in %.2f percent of words" % percentage)
        print()
        print("The letter that is easiest to avoid is", smallest_letter)
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
