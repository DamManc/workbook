# Exercise 137: Two Dice Simulation
import random


def rolling():
    roll = []
    for i in range(2):
        dice = random.randint(1, 6)
        roll.append(dice)
    return sum(roll)


def main():
    # number of roll
    tot_roll = 1000
    # dictionary with results
    table = {}
    # populate dict with key as sum of rolling two dice and value as calc of freq
    for i in range(tot_roll):
        r = rolling()
        table[r] = 1 + table.get(r, 0)
    # transform frequency in percentage relate of totals toss
    for t in table:
        table[t] = [(table[t] / tot_roll) * 100]
    # dictionary with percentage expected by probability theory
    expected = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, \
                7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, \
                11: 2 / 36, 12: 1 / 36}
    # print about table and expected
    print("Total    Simulated       Expected")
    print("           Percent       Percent")
    for k in sorted(table):
        print(f'{k}         {round(table[k][0], 2)}             {round(expected[k] * 100, 2)}')


if __name__ == '__main__':
    main()
