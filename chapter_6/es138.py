# Exercise 138: Text Messaging

def main():
    keypad = {1: ['.', ',', '?', '!', ':'], 2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
              5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'],
              9: ['W', 'X', 'Y', 'Z'], 0: [' ']}
    print('Enter a message')
    usr_input = input()
    message = usr_input.upper()
    keypad_reverse = {}
    for k in keypad:
        for v in keypad[k]:
            if v not in keypad_reverse:
                keypad_reverse[v] = str(k) * (keypad[k].index(v) + 1)
    output = ''
    for ch in message:
        for k in keypad_reverse:
            if ch == k:
                output += keypad_reverse[k]
    print(f'the key presses needed for this message are {output}')


if __name__ == '__main__':
    main()
