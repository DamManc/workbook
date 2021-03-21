# Exercise 90: The Twelve Days of Christmas
import es89

print("The song The Twelve Days of Christmas: ")


def display(n):
    def int_display(n_int):
        if n_int == 2:
            return "Two turtle doves,"
        elif n_int == 3:
            return "Three French hens,"
        elif n_int == 4:
            return "Four calling birds,"
        elif n_int == 5:
            return "Five gold rings,"
        elif n_int == 6:
            return "Six geese a laying,"
        elif n_int == 7:
            return "Seven swans a swimming,"
        elif n_int == 8:
            return "Eight maids a milking,"
        elif n_int == 9:
            return "Nine ladies dancing,"
        elif n_int == 10:
            return "Ten lords a leaping,"
        elif n_int == 11:
            return "Eleven pipers piping,"
        elif n_int == 12:
            return "Twelve drummers drumming,"

    print("On the ", es89.int_to_ord(n), " day of Christmas")
    print("my true love sent to me:")
    if n > 1:
        for i in range(2, (n+1)):
            print(int_display(i))
        print("And a partridge in a pear tree.")
        print()
    else:
        print("A partridge in a pear tree.")
        print()


def main():
    for i in range(1, 13):
        display(i)


main()
