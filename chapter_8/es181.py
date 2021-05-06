quarters = 0.25
dimes = .10
nickels = .05
pennies = .01

def possible_change(dollar_amount):
    n_coins = 0
    if dollar_amount > quarters:
        rem = dollar_amount // quarters
        dollar_amount = dollar_amount - rem * quarters
    elif dollar_amount > dimes:
        rem = dollar_amount // dimes
        dollar_amount = dollar_amount - rem * dimes
    elif dollar_amount > nickels:
        rem = dollar_amount // nickels
        dollar_amount = dollar_amount - rem * nickels
    elif dollar_amount > pennies:
        rem = dollar_amount // pennies
        dollar_amount = dollar_amount - rem * pennies
    n_coins = rem
    if dollar_amount != 0:
        return n_coins + dollar_amount(dollar_amount)
    else:
        return n_coins
        
def main():
    print('Enter a dollar amount (e.g. 1.25)')
    dollar_amount = float(input())
    print('Enter the numbers of coin (e.g. 5)')
    numbers_coin = float(input())
    if possible_change(dollar_amount) == numbers_coin:
        print('YES, the entered dollar amount can be formed using the number of coins indicated.')
    else:
        print('NO, the entered dollar amount can\'t be formed using the number of coins indicated.')


if __name__ == '__main__':
    main()