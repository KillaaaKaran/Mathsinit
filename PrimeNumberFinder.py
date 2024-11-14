import sys

sys.set_int_max_str_digits(999999)

while True:
    x = int(input("Enter a number to check if it's prime: "))
    
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    else:
        print("Not prime")