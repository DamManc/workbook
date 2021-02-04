# Faces on Money
banknote = int(input("Enter the amount of a banknote: "))
if banknote == 1:
    person_face = "George Washington"
elif banknote == 2:
    person_face = "Thomas Jefferson"
elif banknote == 5:
    person_face = "Abraham Lincoln"
elif banknote == 10:
    person_face = "Alexander Hamilton"
elif banknote == 20:
    person_face = "Andrew Jackson"
elif banknote == 50:
    person_face = "Ulysses S.Grant"
elif banknote == 100:
    person_face = "Benjamin Franklin"
else:
    person_face = "has not faces on money"
print("%i %s" % (banknote, person_face))
