#Compound Interest
INTEREST_PER_YEAR = 0.04
money_account = float(input("Enter the amount of money deposited: "))
after_1_year = money_account + (money_account*INTEREST_PER_YEAR)
after_2_year = after_1_year + (after_1_year*INTEREST_PER_YEAR)
after_3_year = after_2_year + (after_2_year*INTEREST_PER_YEAR)
print("After 1 year you have %.2f, after 2 years you have %.2f and after 3 year you have %.2f" %(after_1_year, after_2_year, after_3_year)) 