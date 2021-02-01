#Mailing Adress
name = "Damiano"
adress = "Via Andrea del Verrocchio - n° 114"
print(name, adress)
#Hello
name = input("What's your name? ")
print("Hello", name)
#Area of a room
l = float(input("Length in meters: "))
w = float(input("Width in meters: "))
area = l * w
print("%.2f" % area, 'meters')
#Area of a field
l = float(input("Length in feet: "))
w = float(input("Width in feet: "))
area = (l * w) / 43560
print("%.4f" % area, 'acre')