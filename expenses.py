expenses = [ ]
while True:
    amount = int(input("enter expense amount : "))
    expenses.append(amount)
    choice = input("enter another expenses (yes/no): ")
    if choice == "no":
        break
print("total expenses : ",sum(expenses))
   