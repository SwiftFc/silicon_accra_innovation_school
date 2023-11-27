#Take An Input from the user
#The input will be their exam result
#When the number is given,
#check if the result is an A, B, C, D, F

result = input("Enter Your Result: ")

result = float(result)

if result >= 80:
    print("You got A")

elif result >= 70:
    print("You got B")

elif result >= 60:
    print("You got C")

elif result >= 50:
    print("You got D")

else:
    print("You got F")
