import sys
import random

N_WORDS = 2


def main():
    if len(sys.argv) != 3:
        print('Enter a name of words to create a new Password')
    fin = open(sys.argv[1])
    line = fin.readline()
    lines = []
    while line:
        lines.append(line)
        line = fin.readline()
    password = ''
    for i in range(N_WORDS):
        word = random.choice(lines)
        password += word.replace('\n','').capitalize()
        pos = lines.index(word)
        del lines[pos]
    print(f'Your New Password: {password} ')


if __name__ == '__main__':
    main()
