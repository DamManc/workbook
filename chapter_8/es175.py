
def dec_to_bin(number):
    # base case
    if number == 1:
        return '1'
    elif number == 0:
        return '0'
    else:
        remainder = number % 2 
        quotient = number // 2 
        return str(remainder) + dec_to_bin(quotient)  



def main():
    number = input('Enter a positive decimal number\t')
    if not number:
        print('you have not entered a number')
    else:
        number = int(number)
        if number > 0:
            print(dec_to_bin(number)[::-1])
        else:
            print('You have entered a negative number')
            quit()
    

if __name__ == '__main__':
    main()