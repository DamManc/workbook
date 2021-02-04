# BirthDate to Astrological Sign
month = str(input("Enter a name of a month: "))
day = int(input("Enter a number of a day: "))
if day >= 0 and day <= 31:
    if (month == "December" and day >= 22) or (month == "January" and day <= 19):
        astrological_sign = "Capricorn"
    elif (month == "January" and day >= 20) or (month == "February" and day <= 18):
        astrological_sign = "Aquarius"
    elif (month == "February" and day >= 19) or (month == "March" and day <= 20):
        astrological_sign = "Pisces"
    elif (month == "March" and day >= 21) or (month == "April" and day <= 19):
        astrological_sign = "Aries"
    elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
        astrological_sign = "Taurus"
    elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
        astrological_sign = "Gemini"
    elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
        astrological_sign = "Cancer"
    elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
        astrological_sign = "Leo"
    elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
        astrological_sign = "Virgo"
    elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
        astrological_sign = "Libra"
    elif (month == "October" and day >= 23) or (month == "November" and day <= 22):
        astrological_sign = "Scorpio"
    else:
        astrological_sign = "Sagittarius"
    print("%i %s is sign %s" % (day, month, astrological_sign))
else:
    print("The date entered is incorrect")
