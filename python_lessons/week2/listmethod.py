my_list = [1,2,3,4,5,6,7]
my_list.append(8)
print(my_list)

my_list.insert(4,8)
print(my_list)

my_list.extend([1])
print(my_list)

my_list.extend(["hello", "world"])
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(4)
print(my_list)

my_list.remove('hello')
print(my_list)


#if you want to slice use this format

#lets say a list of [1,2,3,4,5,6,7] and you want to slice at a certain index
#Now lets slice [2,3,4]
#slice stats with the first index plus one


my_list1 = [1,2,3,4,5,6,7]
x = my_list1[1:4][::-1]
print(x)

x = list2 = [1,2,3,4,5,6,7]

x = range(8)
for i in list2:
    print(i)