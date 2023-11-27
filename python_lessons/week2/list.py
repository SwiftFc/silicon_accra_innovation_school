#testing list

list = [1,2,3,4,5,6]

#list comprehension

list1 = [x*2 for x in list]
#print(list1)

list1 = [x*2 for x in list if x > 3]
#print(list1)

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

score = {'kristal': '90%', 'henry': '100%', 'dice': '70'}
for k, v in score.items():
    print(f" {k} got {v}")

x = matrix[0]
#print(x)

x = list
