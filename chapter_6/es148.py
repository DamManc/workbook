# Exercise 148: Play Bingo
from es147 import *
import copy


def main():
    print('Welcome to the Bingo Game!!')
    print('------ Your card ------')
    card = bingo_card()
    print_bingo_card(card)
    n_calls = []
    for i in range(0, 1000):
        copy_card = copy.deepcopy(card)
        gamble = False
        count = 0
        while not gamble:
            numbers = []
            while len(numbers) < 5:
                r = random.randint(1, 75)
                if r not in numbers:
                    numbers.append(r)
            gamble = check_card(copy_card, numbers)
            if gamble:
                print('Your call:', end='\t')
                print(f'{numbers} *****************---> WIN {gamble}')
                print(f'tot calls: {count}')
                n_calls.append(count)
            else:
                count += 1
    print(f'The minimum number of calls is {min(n_calls)}')
    print(f'The maximum number of calls is {max(n_calls)}')
    print(f'The average number of calls is {sum(n_calls) / 1000}')


if __name__ == '__main__':
    main()
