import sys

NUM_LINES = 10


def main():
    if len(sys.argv) != 2:
        print("Provide the file name as a command line argument.")
        quit()
    try:
        fin = open(sys.argv[1], 'r')
        lines = []
        for line in fin:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        fin.close()
        print(''.join(lines))
    except IOError:
        print("An error occurred while accessing the file.")


if __name__ == '__main__':
    main()
