import random

number = random.randint(1, 100)
print("I have picked a number between 1 and 100. Try to guess it!")
guess = int(input("enter your number : "))
while guess != number:
    if guess < number:
        print("Too Low ")
    elif guess > number:
        print("Too High")
    guess = int(input("enter your number : "))
    
print("congratulations you guessed the number ")