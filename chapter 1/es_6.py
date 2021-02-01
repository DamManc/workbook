#Tax and tip
LOCAL_TAX_RATE = 0.22
cost_meal = float(input("How much is cost of the meal? "))
tip = cost_meal * 0.18
tax = cost_meal * LOCAL_TAX_RATE
total_meal = cost_meal + tax + tip
print("The Tip is: %.2f, the Tax is: %.2f, the Total is: %.2f." % (tip, tax, total_meal))
