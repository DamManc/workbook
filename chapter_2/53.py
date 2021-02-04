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
grade_points = float(input("Enter a grade points: "))
if grade_points >= 4.0:
    letter_grade = A_PLUS
elif grade_points < 4.0 and grade_points >= 3.85:
    letter_grade = A
elif grade_points < 3.85 and grade_points >= 3.5:
    letter_grade = A_MIN
elif grade_points < 3.5 and grade_points >= 3.15:
    letter_grade = B_PLUS
elif grade_points < 3.15 and grade_points >= 2.85:
    letter_grade = B
elif grade_points < 2.85 and grade_points >= 2.5:
    letter_grade = B_MIN
elif grade_points < 2.5 and grade_points >= 2.15:
    letter_grade = C_PLUS
elif grade_points < 2.15 and grade_points >= 1.85:
    letter_grade = C
elif grade_points < 1.85 and grade_points >= 1.5:
    letter_grade = C_MIN
elif grade_points < 1.5 and grade_points >= 1.15:
    letter_grade = D_PLUS
elif grade_points < 1.15 and grade_points >= 0.6:
    letter_grade = D
elif grade_points < 0.6 and grade_points >= 0:
    letter_grade = F
else:
    letter_grade = ERROR
if letter_grade == ERROR:
    print("Invalid grade_points, run the program again..")
else:
    print("%.2f is equivalent to %s" % (grade_points, letter_grade))