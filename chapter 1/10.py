#Arithmetic
import math
first_int = int(input("Enter an integer: "))
second_int = int(input("Enter another integer: "))
sum = first_int + second_int
diff_b_a = second_int - first_int
product = first_int * second_int
division = first_int / second_int
remainder = first_int % second_int
log = math.log10(first_int)
exp = first_int ** second_int

print("Sum: %i" %sum)
print("Diff about b and a: %.2f" %diff_b_a)
print("Product: %i" %product)
print("Quotient: %.2f" %division)
print("Remainder: %.2f" %remainder)
print("Log base 10: %.2f" %log)
print("Exp: %i" %exp)
