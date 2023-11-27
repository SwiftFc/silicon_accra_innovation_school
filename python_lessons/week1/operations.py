#TAKE INPUT FROM THE USER
Num1 = input("Enter number1: ")
Num2 = input("Enter number2: ")

Num1 = int(Num1)
Num2 = int(Num2)

add = Num1+Num2
subtract = Num1-Num2
multiply = Num1*Num2
divide = Num1/Num2
modulus = Num1%Num2
mul = Num1*Num2
exp = Num1**2 + Num2
print(f" The addition is: {add}")
print(f" The substraction is: {subtract}")
print(f" The multiplication is: {multiply}")
print(f" The division is: {divide}")
print(f" The modulus is: {modulus}")
print("The multiplication is:", mul)
print("The exponent is:", exp)

if Num1 > Num2:
    print("The Large Number is:", Num1)
else:
    print(Num2)

if Num2 < Num1:
    print("The smaller Number is:", Num2)
else:
    print(Num1)

#Now compare the Numbers if they are true

print("Is the comparison true or false:", Num1 == Num2)
