NATO_phonetic = {'A':'Alpha', 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel',
                'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q': 'Quebec',
                'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

def phonetic_spelling(word):
    # base case
    if word == '':
        return ''
    else:
        result = NATO_phonetic.get(word[0])
        new_word = word[1:]
        return  result + ' ' + phonetic_spelling(new_word) 

def main():
    word = input('Enter a word: ')
    print(phonetic_spelling(word.upper().strip()))


if __name__ == '__main__':
    main()