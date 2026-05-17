a = int(input("enter a number : "))
b = int(input("enter another number : "))
print("\n enter the operation : ")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice = input("enter your choice : ")
if choice == "1":
    print("result : ", a+b)
elif choice == "2":
    print("result : ",a-b)
elif choice == '3':
    print("result : ",a*b)
elif choice == "4":
    print("result : ",a/b)
else:
    print("invalid choice")