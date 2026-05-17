num = int(input("enter a number :"))
if num > 0: 
    print("it is positive number ")
    if num % 2 == 0:
        print("it is a even number")
    else:
        print("it is a odd number ")
elif num < 0:
    print("number is negative")
else:
    print("the number is zero")