# Exercise 125: Shuffling a Deck of Cards
import random


def shuffle(deck):
    new_deck = []
    for card in deck:
        while len(new_deck) != len(deck):
            new_card = deck[random.randrange(0, len(deck))]
            if new_card not in new_deck:
                new_deck.append(new_card)
    return new_deck


def shuffle2(deck):
    for i in range(0, len(deck)):
        r = random.randrange(i, len(deck))
        this_card = deck[i]
        deck[i] = deck[r]
        deck[r] = this_card
    return deck


def create_deck():
    deck = []
    for suit in ["s", "h", "d", "c"]:
        for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            deck.append(value+suit)
    return deck


def main():
    print(f'Deck in order: {create_deck()}')
    print(f'Deck in shuffle: {shuffle(create_deck())}')
    print(f'Deck in shuffle2: {shuffle2(create_deck())}')


if __name__ == '__main__':
    main()
