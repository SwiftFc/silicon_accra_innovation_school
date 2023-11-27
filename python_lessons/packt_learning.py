#How to Use Variable

spent = 3
donated = 4

total_amount = (spent + donated) * 2
print(total_amount)

x = 5
y = 10

sum1 = x + x
sum2 = y + y
print(sum1, sum2)

#Creating a List
student_grade = [20, 6.1, 4.0]

#you can store a list inside a list
student_scores = [9, "Hello", [1,2,3,49,57]] * 3
print(student_scores)

#Creating a list 
student_marks = list(range(0,9))
print(student_marks)

#USE dir function to do all the things for a specific type of data type 
dir(list)
dir(str)
dir(float)

#also use help to a get a method descriptor
help(str.upper)


#Using Dictionaaries in python

student_assignment = {"Henry" : 9.1, "Sam" : 8.0, "Peter": 4.4}

print(student_assignment)#.values())


monday_temperature = [20.1, 23.2, 27.2, 28.3, 25.4]
len(monday_temperature)




#functions in python

def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean
print(mean([20, 30, 50]))

def add():
    mysum = 2 + 5
    
    return mysum

print(add())





#user = input("Say something")
result = " "
while True:
    user = input("Say Something: ")
    if user == "\end":
        break
    else:
        continue
result.__add__
print(result)
def setence_maker(phrase):
    capitalize = phrase.capitalize()
    
