#Get Data of two ranges and find which one has the largest sum and minimum sum

# what is the median, mean, and standard deviation of the two ranges separately

#Merge the two ranges together and find the sum,mean, median,standard deviation and co variance

#Use your own functions to solve this question

data_1 = range(3,100,2)
data_2 = range(0, 200, 3)

#My custom sum fuction defined here
def mysum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

x = mysum(data_1)
y = mysum(data_2)
print("Sum of data_1 is:" ,x)
print("Sum of data_2 is:" ,y)
if x > y:
    print("data_1 is the largest range")
else:
    print("data_2 is the largest range")

#define mean function
def mymean(numbers):
    mean = mysum(numbers) / len(numbers)
    return mean

print("The mean for data_1 is:", (mymean(data_1)))
print("The mean for data_2 is:", (mymean(data_2)))

#define median function
def mymedian(numbers):
    sort = sorted(numbers)
    i = len(sort)
    if i % 2 == 0:
        mid1 = sort[i // 2 - 1]
        mid2 = sort[i // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sort[i // 2]
    return median

print(mymedian(data_1))
print(mymedian(data_2))


# Custom standard deviation function
def custom_std_dev(numbers):
    n = len(numbers)
    if n == 0:
        return 0  # Avoid division by zero for empty lists
    mean = mymean(numbers)
    variance = mysum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5
    return std_dev

print(custom_std_dev(data_1))
print(custom_std_dev(data_2))

