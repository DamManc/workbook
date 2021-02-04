#Vowel or Consonant
letter = str(input("Enter a letter in the latin alphabet: "))
if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
    print("Your letter is vowel")
elif(letter == "y"):
    print("Sometimes y is a vowel, and sometimes y is a consonant")
else:
    print("The letter is a consonant")