import sys

print("Welcome to Karan's (slightly less) Crappy Calculator")
while True:
    True
    x = input("Choose the first number " )
    int(x) and str(x).isdigit()
    y = input("Choose the second number " )
    int(y) and str(y).isdigit()

    if x == "" or y == "":
        print("Please enter a valid number.")

    if not str(x).isdigit() or not str(y).isdigit():
        print("Please enter a valid number.")

    operation = input("Choose the operation you want to perform: +, -, *, /, ^, sqrt " )
    if operation == "+":
        sum = int(x) + int(y)
        print("the sum of " + str(x) + " and " + str(y) + " is: " + str(sum))
    elif operation == "-":
        print("the difference of " + str(x) + " and " + str(y) + " is: " + str(int(x) - int(y)))
    elif operation == "*":
        print("the product of " + str(x) + " and " + str(y) + " is: " + str(int(x) * int(y)))
    elif operation == "/":
        print("the division of " + str(x) + " and " + str(y) + " is: " + str(int(x) / int(y)))
    elif operation == "^":
        print("the power of " + str(x) + " and " + str(y) + " is: " + str(int(x) ** int(y)))
    elif operation == "sqrt":
        print("the square root of " + str(x) + " is: " + str(int(x) ** (1/2)))
        print("the square root of " + str(y) + " is: " + str(int(y) ** (1/2)))


    while True:
        allow = input("Do you want to continue? (y/n) ")
        if str(allow) == "n":
            print("Goodbye!")
            break
            
        elif str(allow) == "y":
            print("Welcome to Karan's (slightly less) Crappy Calculator")
            break
        elif not str(allow) == "y" or str(allow) == "n":
                print("Please enter a valid input.")
                input("Do you want to continue? (y/n) ")
        continue
    True
        
    if __name__ == "__main__":
        pass
