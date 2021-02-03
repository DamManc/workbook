#Wind Chill
air_temp = float(input("Enter an air temperature value in celsius: "))
wind_speed = float(input("Enter an wind speed value in kilometers per hours: "))
WCI = 13.12 + (0.6215 * air_temp) - (11.37 * wind_speed ** 0.16) + (0.3965 * air_temp * wind_speed ** 0.16)
print("The wind Chill Index is: %i" %WCI)