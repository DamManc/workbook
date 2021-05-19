import sys
# FIRST COMMENT
# FIRST COMMENT
# FIRST COMMENT
sys.path.append('/home/dam/code/py/workbook/chapter_2')
from es52 import conver_lett_to_grade
from es53 import conver_grade_to_letter


def main():
    print('Enter a Letter Grades or a Grade Points (blank to finish) and press enter to continue and see the result')
    in_usr = input()
    # FIRST COMMENT
    while in_usr:
        res = []
        try:
            for word in in_usr.split():
                if conver_grade_to_letter(word):
                    res.append(conver_grade_to_letter(word)) # commenting
                elif conver_lett_to_grade(word):
                    res.append(conver_lett_to_grade(word))
                else:
                    raise ValueError
            print(f'the current conversion is {res}')
            # SECOND COMMENT
            in_usr = input()
        except ValueError:
            print('Enter a valid input, blank to finish')
            in_usr = input()


if __name__ == '__main__':
    # FIRST COMMENT
    main()
