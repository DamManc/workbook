# Exercise 140: Postal Codes

def main():
    table = {'Newfoundland': 'A', 'Nova Scotia': 'B', 'Prince Edward Island': 'C', 'New Brunswick': 'E',
             'Quebec': ['G', 'H', 'J'], 'Ontario': ['K', 'L', 'M', 'N', 'P'], 'Manitoba': 'R', 'Saskatchewan': 'S',
             'Alberta': 'T', 'British Columbia': 'V', 'Nunavut': 'X', 'Northwest Territories': 'X', 'Yukon': 'Y'}
    print('Enter a postal code')
    usr_input = input().upper().replace(' ', '')
    if len(usr_input) < 6:
        print('Postal Code not valid')
        exit()
    elif not usr_input[0].isalpha() or not usr_input[2].isalpha() or not usr_input[4].isalpha() or not usr_input[1].isdigit() or not usr_input[3].isdigit() or not usr_input[5].isdigit():
        print('Postal Code not valid')
        exit()
    elif usr_input[0] == 'D' or usr_input[0] == 'F' or usr_input[0] == 'I' or usr_input[0] == 'O' or usr_input[0] == 'Q' or usr_input[0] == 'U' or usr_input[0] == 'W' or usr_input[0] == 'Z':
        print('Postal Code not valid')
        exit()
    else:
        type_addr = ''
        where = ''
        for i in range(len(usr_input)):
            for k in table:
                if table[k] == usr_input[0]:
                    where = k
                if usr_input[1] == '0':
                    type_addr = 'rural'
                else:
                    type_addr = 'urban'
        print(f'that the postal code is for an {type_addr} address in {where}')


if __name__ == '__main__':
    main()