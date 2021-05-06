

def calc_sum(numbers):
    last = len(numbers) - 1
    # base case
    if last == -1:
        return 0
    else: 
        last_number = numbers[last]
        del numbers[last]
        return last_number + calc_sum(numbers)   
        

def main():
    print('Enter a number and press enter: ')
    number = input()
    numbers = []
    if not number:
        print('You don\'t have enter a number')
        print(0.0)
        quit()
    while number:
        numbers.append(int(number))
        print('Enter another number (leave blank to finish)')
        number = input()
    print(f'The sum of this numbers is {calc_sum(numbers)}')



if __name__ == '__main__':
    main()