# Exercise 139: Morse Code

def main():
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                  'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                  'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                  '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                  '8': '---..', '9': '----.'}
    print('Enter a message')
    usr_input = input()
    message = usr_input.upper()
    output = []
    for ch in message:
        for k in morse_code:
            if ch == k:
                output.append(morse_code[k])
    print(' '.join(output))


if __name__ == '__main__':
    main()
