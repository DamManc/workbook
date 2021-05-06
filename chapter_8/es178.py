
def is_palindrome(s):
    # base case
    if s == '':
        return True
    elif len(s) == 1:
        return True
    else:
        check = (s[0] == s[-1])
        new_s = s[1:-1]
        return check and is_palindrome(new_s)

def main():
    s = input('Enter a string: ')
    if is_palindrome(s.upper().strip()):
        print('This string is a palindrome')
    else:
        print('This string is not a palindrome')
if __name__ == '__main__':
    main()