import sys


def main():
    if len(sys.argv) <= 1:
        print("Provide the files names as a command line argument.")
        quit()
    for i in range(1, len(sys.argv)):
        try:
            fin = open(sys.argv[i])
            print(fin.read())
        except IOError:
            print(f"######### An error occurred while accessing the file {sys.argv[i]}.")


if __name__ == '__main__':
    main()
