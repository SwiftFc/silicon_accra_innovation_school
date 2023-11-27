#HOW TO PRINT A SIMPLE STATEMENT USING PYTHON
print("Hello, World")

#Assigning Variables in Python
amount = 0
print("The amount is", amount)


amount = amount + 6 #amount has been increased to 6

if amount >= 6:   #conditional if, else statement set here
    print("I have the amount") 

else:
    print("I dont have the amount")

new = "value " * amount  #Here we multiply the string `value` by `amount`
                       #(which is now increased to 6)
print(new) #it returns `value` 6 times

print(13 / 3) #This returns a float
print(13 // 3)#This returns Quotient of 13 and 3, removal of fractional parts
print(14 % 3) #This returns the integer remainder after division of 14 and 3
print(3 ** 3) #This returns the exponetial value of `3` three times
print(-3)# This returns the negative of 3
print(8 - 3 + 2)

#min and max return the minimum and maximum of their arguments
print(min(4,9,29))
print(max(4,9,29))

#abs returns the absolute value of an argument
print(abs(593))
print(abs(-593))
print(abs(9 + 3))
