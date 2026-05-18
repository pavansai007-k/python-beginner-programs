import random 
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "@#$%&*"
all_chars = letters + numbers + symbols
length = int(input("enter password length : "))
password = ""
for i in range(length):
      password += random.choice(all_chars)

print("Generated password :", password)
            