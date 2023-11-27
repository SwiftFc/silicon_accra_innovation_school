#Take a Paragraph
#Convert it to lowercase
#Count the word "the", "that", "for"
#Replace all the occurence of "the", "that", "for" with "YAY"
#count the total length of the paragraph
#count the number of spaces in the paragraph

para = """A for loop in Python is a programming construct that allows you to iterate over a sequence of objects. For example, you can use a for loop to iterate over a list, a string, or a set.
To use a for loop, you first need to define the sequence that you want to iterate over. Then, you need to define a variable to store the current element of the sequence.
"""

print(para)

#Now print in lower case

print(para.lower())

#Count the word "the", "that, "for"

print("The number of `the` is:", para.count('the'))
print("The number of `that` is:", para.count('that'))
print("The number of `for` is:", para.count('for'))

#Now replace all the occurence of "the, that, for" in the paragraph
#with "YAY"

#Assign a variable that will handle this
x = para.replace("the", "YAY")
y = x.replace("that", "YAY")
z = y.replace("for", "YAY")
print(z)

#Now find the total length of the paragraph

print("The total length of the paragraph is:", len(para))

#Count the number of space in the entire paragraph

print("The total number of spaces is:", para.count(" "))
