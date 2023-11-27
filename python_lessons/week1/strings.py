#Take inputs from the user
#Take the name of the user
#Take the location of the user
#Dream Car of the User
#Favorite Statement of the user

#Assignment
#1. print in lowercase
#2. print in uppercase
#3. check the length of the string
#4. find whether there is a letter `q` in the strings

name = input("Enter Your Name: ")
location = input("Enter Your Location: ")
car = input("Enter your Dream Car: ")
statement = input("Enter your favorite Statement: ")

text = f"my name is {name} and I live in {location} and my favorite car is {car}, now my favorite statement is {statement}"

print(text)
print(text.lower())
print(text.upper())
print(len(text))
print(text.find("q"))
