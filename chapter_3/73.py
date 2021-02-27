# Caesar Cipher
message = input("Your message: ")
shift = int(input("shift amount: "))
new_message = ""
for ch in message:
    if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        pos = ord(ch)
        new_char = chr(pos + shift)
        new_message += new_char
    else:
        new_message += ch
print("The shifted message is", new_message)
