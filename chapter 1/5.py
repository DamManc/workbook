#Bottle Deposits
small_dep = 0.10
big_dep = 0.25
small_cont = float(input("How many container that are less or equal to 1 (only numbers)? "))
big_cont = float(input("How many others big containers (only numbers)? "))
s_ref = small_cont * small_dep
b_ref = big_cont * big_dep
tot_dep = s_ref + b_ref
print("Your total refund is: %.2f$" % tot_dep)