# Exercise 146: Create a Bingo Card
import random


def bingo_card():
    card = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    init = 1
    limit = 15
    for k in card:
        while len(card[k]) < 15:
            r = random.randint(init, limit)
            if r not in card[k]:
                card[k].append(r)
        init += 15
        limit += 15
    return card


def print_bingo_card(card):
    for k in card:
        print(k, end='\t')
    print()
    for i in range(0, 15):
        for k in card:
            print(card[k][i], end='\t')
        print()


def main():
    card = bingo_card()
    print_bingo_card(card)


if __name__ == '__main__':
    main()
