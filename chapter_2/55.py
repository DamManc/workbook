# Wavelengths of Visible Light
VIOLET = 380
BLUE = 450
GREEN = 495
YELLOW = 570
ORANGE = 590
RED = 620
MAX = 750
wavelength = int(input("Enter a wavelength: "))
if wavelength > VIOLET and wavelength <= MAX:
    if wavelength >= VIOLET and wavelength < BLUE:
        color = "VIOLET"
    elif wavelength >= BLUE and wavelength < GREEN:
        color = "BLUE"
    elif wavelength >= GREEN and wavelength < YELLOW:
        color = "GREEN"
    elif wavelength >= YELLOW and wavelength < ORANGE:
        color = "YELLOW"
    elif wavelength >= ORANGE and wavelength < RED:
        color = "ORANGE"
    else:
        color = "RED"
    print("%i is associated with %s color" % (wavelength, color))
else:
    print("This wavelength entered is outside of the visible spectrum")