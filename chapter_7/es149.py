import sys

NUM_LINES = 10


def main():
    if len(sys.argv) != 2:
        print("Provide the file name as a command line argument.")
        quit()

    try:
        fin = open(sys.argv[1], "r")
        line = fin.readline()
        count = 0
        while count < NUM_LINES and line:
            line = line.rstrip()
            count += 1
            print(line)
            line = fin.readline()
        fin.close()
    except IOError:
        print("An error occurred while accessing the file.")


if __name__ == '__main__':
    main()
