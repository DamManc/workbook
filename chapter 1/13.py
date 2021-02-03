#Making Change
penny = 1
nickels = 5
dimes = 10
quarters = 25
loonies = 100
toonies = 200
money_user = int(input("Enter a number of cents: "))
toonies_user = money_user // toonies
remainder_toonies = money_user % toonies
loonies_user = remainder_toonies // loonies
remainder_loonies = remainder_toonies % loonies
quarters_user = remainder_loonies // quarters
remainder_quarters = remainder_loonies % quarters
dimes_user = remainder_quarters // dimes
remainder_dimes = remainder_quarters % dimes
nickels_user = remainder_dimes // nickels
remainder_nickels = remainder_dimes % nickels
penny_user = remainder_nickels // penny
remainder_penny = remainder_nickels % penny

print("The changes is: %i Toonies, %i Loonies, %i Quarters, %i Dimes, %i Nickels, %i Penny" %(toonies_user, loonies_user, quarters_user, dimes_user, nickels_user, penny_user))

