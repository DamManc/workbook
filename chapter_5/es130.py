# Exercise 130: Unary and Binary Operators
from es129 import token


def mark_unary(t):
    op_unary = ('+', '-')
    operator = ('-', '+', '*', '/', '^')
    if t[0] in op_unary:
        t[0] = 'u' + t[0]
    i = 1
    while i < len(t):
        if ((t[i - 1] in operator) or (t[i - 1] == '(')) and (t[i] in op_unary):
            t[i] = 'u' + t[i]
        i += 1
    return t


def main():
    print('Enter a string containing mathematical expression')
    i = input()
    print(mark_unary(token(i)))


if __name__ == '__main__':
    main()
