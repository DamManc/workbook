# Exercise 131: Infix to Postfix
import sys
sys.path.append('/home/dam/code/py/workbook/chapter_4')
from es129 import token
from es130 import mark_unary
from es96 import is_integer
from es97 import precedence_unary


def in_to_post(list):
    operators = []
    postfix = []
    for token in list:
        if is_integer(token):
            postfix.append(token)
        if token == '+' or token == '-' or token == '/' or token == '*':
            while operators and operators[-1] != '(' and precedence_unary(token) < precedence_unary(operators[-1]):
                postfix.append(operators[-1])
                del operators[-1]
            operators.append(token)
        if token == '(':
            operators.append(token)
        if token == ')':
            while operators[-1] != '(':
                postfix.append(operators[-1])
                del operators[-1]
            operators.remove('(')

    while operators:
        postfix.append(operators[-1])
        del operators[-1]
    return postfix


def main():
    print('Enter a string containing mathematical expression')
    i = input()
    print(in_to_post(mark_unary(token(i))))


if __name__ == '__main__':
    main()

