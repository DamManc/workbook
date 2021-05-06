ROMAN_numbers = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def rom_to_int(number):
    # base case
    if number == '':
        return 0
    else:  
        result = ROMAN_numbers.get(number[0])
        if len(number) > 1 and result < ROMAN_numbers.get(number[1]):
            result = ROMAN_numbers.get(number[1]) - result
            new_number =  number[2:]
        else:
            new_number =  number[1:]
        return result + rom_to_int(new_number)


def main():
    number = input('Enter a roman number: ')
    if not number:
        print('you have not entered a number')
    else:
        number = rom_to_int(number.upper().strip())
        print(number)

if __name__ == '__main__':
    main()