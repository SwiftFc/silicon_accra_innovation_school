import random

print("Welcome to number guessing game!!")
x = input("\nEnter Your name to Login: ")

if x.isalpha() != True:  #Setting a condition that allows the user to only enter characters
    print("Invalid Format *** Only accepting Characters")

else:
    print("Login Successful")

num = (1,2,3,4,5,6,7,8,9,10)

num = int(input("Enter Any Number from 1 to 10: "))

i = num
if i.isdigit() != True:
    print("Invalid")

else:
    print("Success")
    #while num <= 10:
        #t = random.choice(num)
        #print(t)




