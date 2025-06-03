while True:    
    print ("Welcome to Karan's Quadratic Equation Solver")
    Two = int(input("Choose the first number that is the coefficient of x² " ))
    One = int(input("Choose the second number that is the coefficient of x " ))
    Zero = int(input("Choose the third number that is the constant " ))

    if Two == "0":
        print ("This is not a quadratic equation")
        exit()
    else:
        print ("This is a quadratic equation")
        break
try:
    Two = int(Two)
    One = int(One)
    Zero = int(Zero)
except ValueError:
    print("Please enter a valid number")
else:
    if str(Two).isdigit() and str(One).isdigit() and str(Zero).isdigit():
        Two = int(Two)
        One = int(One)
        Zero = int(Zero)
    else:
        print ("Please enter a number")
    print("Please enter a valid number")

print ("The equation is: " + str(Two) + "x² + " + str(One) + "x + " + str(Zero) + " = 0")
print ("The discriminant is: " + str(One**2 - 4*Two*Zero))
if One**2 - 4*Two*Zero > 0:
    print ("The equation has two real roots")
elif One**2 - 4*Two*Zero == 0:
    print ("The equation has one real root")
elif One**2 - 4*Two*Zero < 0:
    print ("The equation has no real roots")

    if One**2 - 4*Two*Zero < 0:
        complexroot1 = (-One + (One**2 - 4*Two*Zero)**0.5) / (2*Two)
        complexroot2 = (-One - (One**2 - 4*Two*Zero)**0.5) / (2*Two)
        print ("The roots are: " + str(complexroot1) + " and " + str(complexroot2))

if One**2 - 4*Two*Zero > 0:
    root1 = (-One + (One**2 - 4*Two*Zero)**0.5) / (2*Two)
    root2 = (-One - (One**2 - 4*Two*Zero)**0.5) / (2*Two)
    print ("The roots are: " + str(root1) + " and " + str(root2))

if One**2 - 4*Two*Zero == 0:
    root1 = (-One + (One**2 - 4*Two*Zero)**0.5) / (2*Two)
    root2 = (-One - (One**2 - 4*Two*Zero)**0.5) / (2*Two)
    print ("The roots are: " + str(root1) + " and " + str(root2))

print ("The turning point is " + str(-One/(2*Two)) + "," + str((One**2 - 4*Two*Zero)/(4*Two)))
allow = input("Do you want to exit? (yes/no): ").strip().lower()
if allow == "no":
    print ("You chose to stay!")
    False #go to ln 4 like why cant it just do that??
elif allow == "yes":
    print ("Goodbye!")
    False
    if __name__ == "__main__":
        pass