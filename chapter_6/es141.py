# Exercise 141: Write out Numbers in English

def main():
    print('Enter a number between 0 - 999 to see it in english')
    usr_input = input()
    table = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
             20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
             90: 'ninety'}
    output = ''
    if usr_input:
        # check if user typing is integer and 0 < x < 999
        try:
            n = int(usr_input)
            if 0 < n < 999:
                hundreds = int(n / 100)
                if hundreds > 0:
                    n = n - hundreds * 100
                dozens = int(n / 10)
                dozens_t = 0
                if dozens > 1:
                    dozens_t += dozens * 10
                    n = n - dozens * 10
                for k in table:
                    if hundreds == k:
                        output += f'{table[k]} hundred '
                    if dozens_t == k:
                        output += f'{table[k]} '
                for k in table:
                    if n == k:
                        output += table[k]
            else:
                print('you input is not valid (< 0 or >999)')
                exit()
        except ValueError:
            print('you input is not integer')
            exit()
    else:
        print('you have not insert a value')
        exit()
    print(output)


if __name__ == '__main__':
    main()
