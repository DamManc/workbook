# Discount Table

for i in range(5):
    merc_original = 4.95 + (5 * i)
    merc_discount = merc_original * 0.6
    new_price = merc_original - merc_discount
    print("Orignal: %.2f, WithDiscount: %.2f" % (merc_original, new_price))
