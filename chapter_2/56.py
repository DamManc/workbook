# Frequency to Name
MICROWAVES = 3 * 10e9
INFRARED_LIGHT = 3 * 10e12
VISIBLE_LIGHT = 4.3 * 10e14
ULTRAVIOLET_LIGHT = 7.5 * 10e14
X_RAYS = 3 * 10e17
GAMMA_RAYS = 3 * 10e19
frequency = float(input("Enter a frequency of some radiation: "))
if frequency < MICROWAVES:
    name = "RADIO WAVES"
elif frequency < INFRARED_LIGHT:
    name = "MICROWAVES"
elif frequency < VISIBLE_LIGHT:
    name = "INFRARED_LIGHT"
elif frequency < ULTRAVIOLET_LIGHT:
    name = "VISIBLE_LIGHT"
elif frequency < X_RAYS:
    name = "ULTRAVIOLET_LIGHT"
elif frequency < GAMMA_RAYS:
    name = "X_RAYS"
else:
    name = "GAMMA_RAYS"
print("%.2f have %s name" % (frequency, name))
