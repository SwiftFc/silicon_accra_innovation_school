import csv


"""file = open("./resources/movies.txt", "a")
print(file.name)
#print(file.read())
#for line in file:
#   print(line)

print(file.mode)
file.write("Hello WWorld\n")
file.close()


try:
    
    with open("./resources/movies.txt", "r") as file:
        print(file.name)
        file.read()
        file.write("hello world")
except FileNotFoundError:
    print("Invalid")"""

#file = open("./resources/movies.csv")
with open("./resources/movies.csv", "r") as movies:
    #print(file.name)
    #print(file.read())
    info = csv.reader(movies)
    for record in info:
        title , rating, year, runtime = record
        print(f" {title, rating, year, runtime}")