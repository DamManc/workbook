# Parity Bits
input_user = input("Enter a string (balnk to quit): ")
while input_user != "":
    bits = input_user.count(input_user)
    if bits.count("0") + bits.count("1") != 8 or len(bits) != 8:
        print("That wasn’t 8 bits... Try again.")
    else:
        ones = bits.count("1")
    if ones % 2 == 0:
        print("The parity bits should be 0")
    else:
        print("The parity bits should be 1")
    input_user = input()
