# Exercise 126:Dealing Hands of Cards
from es125 import *
import random


def deal(hands, cards, deck):
    tot_hands = []
    for h in range(0, hands):
        hand = []
        for i in range(0, cards):
            r = random.randrange(0, len(deck))
            card = deck[r]
            hand.append(card)
            del deck[r]
        tot_hands.append(hand)
    return tot_hands


def main():
    hands = 4
    cards = 5
    deck = shuffle(create_deck())
    tot_hands = deal(hands, cards, deck)
    for hands in tot_hands:
        c = 0
        while c != len(hands):
            print(f'For Player {c}: {hands[c]}')
            c += 1


if __name__ == '__main__':
    main()
