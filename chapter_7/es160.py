import sys
import re


def weird_words(words):
    ie_ei_words = [word for word in words if re.search('(ei)|(ie)', word)]
    yes_rules = []
    no_rules = []
    for word in ie_ei_words:
        if re.search('(cei)|(ie)', word):
            yes_rules.append(word)
        else:
            no_rules.append(word)
    return yes_rules, no_rules


def main():
    if len(sys.argv) != 2:
        print('You must insert the file to read')
        quit()
    try:
        fin = open(sys.argv[1], 'r')
        line = fin.readline()
        words = []
        while line:
            for word in line.split():
                if word.lower() not in words:
                    words.append(word.lower())
            line = fin.readline()
        check_rule = weird_words(words)
        print(f'Words that follow the rule: {check_rule[0]}')
        print(f'Words that not follow the rule: {check_rule[1]}')
    except IOError:
        print(f"An error occurred while accessing the file {sys.argv[1]}.")


if __name__ == '__main__':
    main()
