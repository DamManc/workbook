ship_charge = 10.95
SUBSEQUENT_ITEM = 2.95
n_items = int(input("enter the numbers of items in the order: "))


def main(n_items):
    while n_items != 0:
        global ship_charge
        ship_charge += (n_items - 1) * SUBSEQUENT_ITEM
        n_items = 0
    print(ship_charge)


main(n_items)