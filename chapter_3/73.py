# Caesar Cipher
message = input("Your message: ")
shift = input("shift amount: ")
shift_n = int(shift)
s = list(message)
i = 0
for i in range(len(message)):
    s[i] = s[i + shift_n]
print(s)
