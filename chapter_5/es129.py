# Exercise 129:Tokenizing a String


def token(input):
    s = input.replace(' ', '')
    operator = ('-', '+', '*', '/', '^')
    parenthesis = ('(', ')', '[', ']', '{', '}')
    i = 0
    token = []
    while i < len(s):
        if s[i] in operator or s[i] in parenthesis:
            token.append(s[i])
            i += 1
        elif '0' <= s[i] <= '9':
            token_digit = []
            while i < len(s) and '0' <= s[i] <= '9':
                token_digit.append(s[i])
                i += 1
            token.append(''.join(token_digit))
        else:
            return 'Your input is not valid..'
    return token


def main():
    print('Enter a string containing mathematical expression')
    i = input()
    print(token(i))


if __name__ == '__main__':
    main()
