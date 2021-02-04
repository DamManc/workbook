# Note to Frequency
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
note = str(input("Enter a name of a note: "))
octave = int(input("Enter the octave: "))
if note == "C":
    ref_freq = C4
    freq = ref_freq / 2 ** (4 - octave)
elif note == "D":
    ref_freq = D4
    freq = ref_freq / 2 ** (4 - octave)
elif note == "E":
    ref_freq = E4
    freq = ref_freq / 2 ** (4 - octave)
elif note == "F":
    ref_freq = F4
    freq = ref_freq / 2 ** (4 - octave)
elif note == "G":
    ref_freq = G4
    freq = ref_freq / 2 ** (4 - octave)
elif note == "A":
    ref_freq = A4
    freq = ref_freq / 2 ** (4 - octave)
else:
    ref_freq = B4
    freq = ref_freq / 2 ** (4 - octave)
print("The %s%i have %3.02f frequency" % (note, octave, freq))
