import random
import datetime
import time

print("""
number guessing game
Guess the number in the range 1-10
""")
estimated_number = input("Please enter number :")

nunbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


estimated_number = int(estimated_number)

random_number = (random.choice(nunbers))

if random_number == estimated_number:
    print("right guess")

elif estimated_number == 10:
    print("The number 10 is invalid 1-9")

elif random_number != estimated_number:
    print("wrong guess")

    time.sleep(1)

    print("correct number")
    print(random_number)
