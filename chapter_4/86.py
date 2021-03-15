BASE_FARE = 4.00
PLUS = 0.25
METRES_PLUS = 140
km_done = float(input("Enter the number of km: "))


def main(distance):
    dist_m = distance * 1000
    plus_fare = dist_m // METRES_PLUS
    print(plus_fare)
    tot = BASE_FARE + plus_fare * 0.25
    print("The total fare is %.2f" % tot)


main(km_done)