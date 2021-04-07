# Exercise 97: Operator Precedence
def precedence(n):
    if n == '+' or n == '-':
        return 1
    elif n == '*' or n == '/':
        return 2
    elif n == '^':
        return 3
    else:
        return -1


def precedence_unary(n):
    if n == '+' or n == '-':
        return 1
    elif n == '*' or n == '/':
        return 2
    elif n == 'u+' or n == 'u-':
        return 3
    elif n == '^':
        return 4
    else:
        return -1


def main():
    op = input("Enter an operator: ")
    if precedence(op) != -1:
        print(f'The operator\'s precedence is {precedence(op)}')
    else:
        print('Your entered input is not valid')


if __name__ == '__main__':
    main()
