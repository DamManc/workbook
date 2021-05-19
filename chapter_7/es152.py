import sys


def main():
    if len(sys.argv) != 3:
        print('You must enter the name of file to open and the name of file to create')
        quit()
    try:
        fin = open(sys.argv[1], "r")
        fout = open(sys.argv[2], "w+")
        lines = fin.readlines()
        for i in range(len(lines)):
            lines[i] = f'{i}: ' + lines[i]
            fout.write(lines[i])
        # the file's object index needs to be moved to the beginning
        fout.seek(0)
        print(fout.read())
        fin.close()
        fout.close()
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
