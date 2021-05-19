# Letter Grade to Grade Points
A = 4.0
A_MIN = 3.7
B_PLUS = 3.3
B = 3.0
B_MIN = 2.7
C_PLUS = 2.3
C = 2.0
C_MIN = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
ERROR = -1


def conver_lett_to_grade(letter_grade):
    if letter_grade == "A+" or letter_grade == "A":
        grade_points = A
    elif letter_grade == "A-":
        grade_points = A_MIN
    elif letter_grade == "B+":
        grade_points = B_PLUS
    elif letter_grade == "B":
        grade_points = B
    elif letter_grade == "B-":
        grade_points = B_MIN
    elif letter_grade == "C+":
        grade_points = C_PLUS
    elif letter_grade == "C":
        grade_points = C
    elif letter_grade == "C-":
        grade_points = C_MIN
    elif letter_grade == "D+":
        grade_points = D_PLUS
    elif letter_grade == "D":
        grade_points = D
    elif letter_grade == "F":
        grade_points = F
    else:
        grade_points = ERROR
    if grade_points == ERROR:
        return False
    else:
        return grade_points


def main():
    letter_grade = input("Enter a letter grade: ")
    if conver_lett_to_grade(letter_grade):
        print("%s is equivalent to %.1f" % (letter_grade, conver_lett_to_grade(letter_grade)))
    else:
        print("Invalid letter grade, run the program again..")


if __name__ == '__main__':
    main()
