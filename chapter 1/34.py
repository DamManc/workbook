#Day Old Bread
L_BREAD = 3.49
DIS_OLD = 0.60
n_loa = int(input("Enter the number of loaves: "))  
regu_price = n_loa * L_BREAD
disc =regu_price * DIS_OLD
tot = regu_price - disc
print("Regular price for these loaves: %.2f" %regu_price)
print("Discount for these loaves: %.2f" %disc)
print("Total price for these loaves: %.2f" %tot)