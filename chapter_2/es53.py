# Grade Points to Letter Grade
A_PLUS = "A+"
A = "A"
A_MIN = "A-"
B_PLUS = "B+"
B = "B"
B_MIN = "B-"
C_PLUS = "C+"
C = "C"
C_MIN = "C-"
D_PLUS = "D+"
D = "D"
F = "F"
ERROR = ""


def conver_grade_to_letter(grade_points):
    try:
        grade_points = float(grade_points)
    except ValueError:
        return False
    if grade_points == 4.0:
        letter_grade = A_PLUS
    elif 4.0 > grade_points >= 3.85:
        letter_grade = A
    elif 3.85 > grade_points >= 3.5:
        letter_grade = A_MIN
    elif 3.5 > grade_points >= 3.15:
        letter_grade = B_PLUS
    elif 3.15 > grade_points >= 2.85:
        letter_grade = B
    elif 2.85 > grade_points >= 2.5:
        letter_grade = B_MIN
    elif 2.5 > grade_points >= 2.15:
        letter_grade = C_PLUS
    elif 2.15 > grade_points >= 1.85:
        letter_grade = C
    elif 1.85 > grade_points >= 1.5:
        letter_grade = C_MIN
    elif 1.5 > grade_points >= 1.15:
        letter_grade = D_PLUS
    elif 1.15 > grade_points >= 0.6:
        letter_grade = D
    elif 0.6 > grade_points >= 0:
        letter_grade = F
    else:
        letter_grade = ERROR
    if letter_grade == ERROR:
        return False
    else:
        return letter_grade


def main():
    grade_points = input("Enter a grade points: ")
    if conver_grade_to_letter(grade_points):
        print("%.2f is equivalent to %s" % (grade_points, conver_grade_to_letter(grade_points)))
    else:
        print("Invalid grade_points, run the program again..")


if __name__ == '__main__':
    main()
