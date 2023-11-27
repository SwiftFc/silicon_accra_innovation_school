import random

"""
main - A program where a computer generates
a random number and a user has to guess the number
"""

"""
Keywords - random, number,
user input, guess,
for loop, 
conditions, 
range
"""

x = input("Guess the Number: ")

x = int(x)

x = [1,2,3,4,5,6,7,8,9]

x = random.choice(x)

print(f"The computerised random number is:", x)
