# Exercise 145: Scrabble™ Score
def scrabble(s):
    score = 0
    table = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
             4: ['F', 'H', 'V', 'W', 'Y'], 5: 'K', 8: ['J', 'X'], 10: ['Q', 'Z']}
    table_rev = {}
    for k in table:
        for i in range(0, len(table[k])):
            if table[k][i] not in table_rev:
                table_rev[table[k][i]] = k
    for ch in s.upper():
        for k in table_rev:
            if ch == k:
                score += table_rev[k]
    return score


def main():
    print('Enter a word')
    usr_input = input()
    while len(usr_input.split()) > 1:
        print('Only one word pls.')
        usr_input = input()
    print(f'The Scrabble score is {scrabble(usr_input)}')


if __name__ == '__main__':
    main()
