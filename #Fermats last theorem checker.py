#Fermats last theorem checker
import sys
print("Fermat's Last Theorem Checker by Karan Dahyea")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
n = int(input("Enter n (n > 2): "))
if n <= 2:
    print("n must be greater than 2.")
else:
    left_side = a**n + b**n
    right_side = c**n
    if left_side == right_side:
        print("Fermat's Last Theorem is violated: a^n + b^n = c^n")
    else:
        print("Fermat's Last Theorem holds: a^n + b^n != c^n")

if a == 0 or b == 0 or c == 0:
    print("One of the inputs is zero, which is not valid for Fermat's Last Theorem.")

an = a**n
bn = b**n
cn = a**n + b**n


print(str(cn) + " is not equal to " + str(an) + " + " + str(bn))