# Exercise 132: Evaluate Postfix
from es129 import token
from es130 import mark_unary
from es131 import in_to_post


def eval_post(list):
    values = []
    for token in list:
        if token.isdigit():
            values.append(int(token))
        elif token == 'u-':
            last_item = values[-1]
            del values[-1]
            values.append(-last_item)
        elif token == '+' or token == '-' or token == '*' or token == '/' or token == '^':
            right = values[-1]
            del values[-1]
            left = values[-1]
            del values[-1]
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            else:
                result = left ** right
            values.append(result)
    return values[0]


def main():
    print('Enter a string containing mathematical expression')
    i = input()
    print(eval_post(in_to_post(mark_unary(token(i)))))


if __name__ == '__main__':
    main()
