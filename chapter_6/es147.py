# Exercise 147: Checking for a Winning Card
from es146 import *


def check_card(card, numbers):
    # assigns the numbers gambled by the player to 0
    for n in numbers:
        for k in card:
            if n in card[k]:
                index_to0 = card[k].index(n)
                card[k][index_to0] = 0

    line = False
    # check Vertical line of 0
    for k in card:
        for i in range(5, len(card[k])):
            if (card[k][i - 5] + card[k][i - 4] + card[k][i - 3] + card[k][i - 2] + card[k][i - 1]) == 0:
                line = 'Vertical'
    # check Horizontal line of 0
    for i in range(15):
        v = 0
        for k in card:
            v += card[k][i]
        if v == 0:
            line = 'Horizontal'
    # check Diagonal Left line of 0
    for i in range(11):
        v = 0
        ind = i
        for k in card:
            v += card[k][ind]
            ind += 1
        if v == 0:
            line = 'Left Diagonal'
    # check Diagonal Right line of 0
    for i in range(11):
        v = 0
        ind = i
        for k in reversed(card):
            v += card[k][ind]
            ind += 1
        if v == 0:
            line = 'Right Diagonal'
    return line


def main():
    print('Welcome to the Bingo Game!!')
    print('------ Your card ------')
    card = bingo_card()
    print_bingo_card(card)
    print('Enter a five numbers between (1 - 75) and press enter to submit')
    usr_numbers = []
    while len(usr_numbers) != 5:
        usr_input = input()
        if len(usr_input.split()) != 5:
            print('Not valid input')
            continue
        for number in usr_input.split():
            try:
                x = int(number)
                if 0 < x <= 75 and x not in usr_numbers:
                    usr_numbers.append(x)
                else:
                    usr_numbers.clear()
                    print('One number are not valid (< 1 or > 75) or you have insert numbers equals')
                    break
            except ValueError:
                print('Enter five numbers pls')
                break
    if check_card(card, usr_numbers):
        print(f'YOU WIN!!!! {check_card(card, usr_numbers)}')
    else:
        print('Sorry, you lose..')


if __name__ == '__main__':
    main()
