import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("enter rock,paper,scissors : ").lower()
print("computer chose : ",computer)

if user == computer:
    print("wow! it,s a tie")
elif user == "rock" and computer == "scissor":
    print("congrats !!,you won ")
elif user == "paper" and computer == "rock":
    print("congrats !!,you won ")
elif user == "scissor" and computer == "paper":
     print("congrats !!,you won ")
elif user in choices :
    print("ohh!!, computer won")
else:
    print("invalid input")
    
