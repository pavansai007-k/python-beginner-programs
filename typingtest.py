import time 
print("----typing speed test----")
sentence = "python is easy to learn"
print("\ntype this exactly")
print(sentence)
input("\npress enter to start")
start_time = time.time()
typed = input("\nstart typing : ")
end_time = time.time()
time_taken = end_time - start_time
words = len(sentence.split())
speed = (words/time_taken)*60
print(f"time taken: {round(time_taken, 2)} seconds")
print(f"typing speed: {round(speed, 2)} words per minute")
if typed == sentence:
    print("accuarcy ia 100%")
else:
    print("some are mistake.")