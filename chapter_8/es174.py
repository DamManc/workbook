
def greatest_cdivisor(numbers):
    a = numbers[0]
    b = numbers[1]
    if b == 0:
        return a
    else:
        c = a % b
        return greatest_cdivisor([b, c])




def main():
    numbers = []
    max = 2 # input of two number  
    while max:
        print('Enter a number')
        number = input()
        try:
            number = int(number)
            numbers.append(number)
            max -= 1
        except ValueError:
            print('This is not a number')
    print(f'The greatest common divisor is {greatest_cdivisor(numbers)}')
    
        
    


if __name__ == '__main__':
    main()