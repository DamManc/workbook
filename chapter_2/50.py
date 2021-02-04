# Richter Scale
magnitude = float(input("Enter a magnitude value: "))
if magnitude < 2.0:
    descriptor = "Micro"
elif magnitude < 3.0:
    descriptor = "Very Minor"
elif magnitude < 4.0:
    descriptor = "Minor"
elif magnitude < 5.0:
    descriptor = "Light"
elif magnitude < 6.0:
    descriptor = "Moderate"
elif magnitude < 7.0:
    descriptor = "Strong"
elif magnitude < 8.0:
    descriptor = "Major"
elif magnitude < 10:
    descriptor = "Great"
else:
    descriptor = "Meteoric"
print(
    "Magnitude %.2f earthquake is considered to be a %s earthquake"
    % (magnitude, descriptor)
)
