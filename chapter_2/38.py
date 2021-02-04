# Name That Shape
number_of_sides = int(input("Enter a number of sides from 3 to 10: "))
if number_of_sides >= 3 and number_of_sides <= 10:
    if number_of_sides == 3:
        name = "Triangolo"
    elif number_of_sides == 4:
        name = "Quadrilatero"
    elif number_of_sides == 5:
        name = "Pentagono"
    elif number_of_sides == 6:
        name = "Esagono"
    elif number_of_sides == 7:
        name = "Ettagono"
    elif number_of_sides == 8:
        name = "Ottagono"
    elif number_of_sides == 9:
        name = "Ennagono"
    else:
        name = "Decagono"
    print("The appropriate name for your polygon is: %s " % name)
else:
    print("Your integers is not correct, run the program again")