<<<<<<< HEAD
#Take the list of students in Silicon Accra Class
#print out the total number of students
#shuffle the list of students
#pick a random student out of the list
#add a 2 new student to the list

import random
student_name = ["Kristal",
                "Henry",
                "Abena",
                "Stanley",
                "Nehemiah",
                "Precious",
                "Stephen",
                "praiz",
                "Stanley"]

for name in student_name:
    print(name)

x = student_name.index("Abena")
print("\n", x)

random.shuffle(student_name)
for name in student_name:
    print("\nThe shuflle list is:", name)

new = random.choice(student_name)

print("\nThe random choice is:", new)
=======
import random

#randint
#randrange
#choice
#shuffle

student_name = ["Kristal" "Henry", "Stephen", "Abena", 
                "Precious", 
                "Nehemiah"]

student_name.extend(["Maya",
                     "Caleb"])

#Before Shuffling

for i in student_name:
    print(i)


for name in student_name:
    print("The names of student are:", name)

random.shuffle(student_name)
for name in student_name:
    print("\nThe shuffle names are:", name)

new = random.choice(student_name)

print("The random name is:", new)



>>>>>>> 43758d496e60f0f68e060633cd92aa30ff44a155
