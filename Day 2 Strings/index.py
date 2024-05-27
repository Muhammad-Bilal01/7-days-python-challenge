# print("Welcome to Day 2")

# String in python
# str1 = 'I am String with single Quotes'
# str2 = 'I am String with double Quotes'
# str3 = '''I am Multi
# line String encloesed with 
# single/double three inverted quotes
# '''

# print(str1)
# print(str2)
# print(str3)

# Use escape sequense
#  - give extra information or allow special characters to print in our string

# str = "My name is Muhammad Bilal.\nI am a student of SMIU"
# print(str)


# Indexing and Slicing

# Index
# str = "My name is Muhammad Bilal"
# we can access single character of String with [index]. start with 0.

# print(str[1])

# we cannot change any character using index
# str[5] = "w" #'str' object does not support item assignment
# print(str)


# Slicing

# by using slicing we can get multiple characters of the string from a particular range.

# print(str[0:8]) # end is not included!
# print(str[0:]) # start with zero and end length like [0:len(str)]
# print(str[:8]) # default start with zero

# Negative Indexing
# name = "Bilal"
# B:-5 i: -4 l: -3 a: -2  l: -1
# print(name[-5:-1]) # for reverse printing

# String Method 

str = "My name is Muhammad Bilal"
# print("Length of String",len(str),"type of String",type(str))

# String Concatenation

# firstName = "Muhammad" 
# lastName = "Bilal" 
# fullName = firstName + " " + lastName
# print(fullName) 


# str = "my Name is Bilal"
# print(str.capitalize())
# print(str.count("B"))
# print(str.endswith("yl"))
# print(str.replace("a","e"))
# print(str.replace("Bilal","Noman"))
# print(str.find("is"))


# Conditional Statement

# if - elif - else

# marks = int(input("Enter your Marks: "))

# if(marks >= 90 and marks <= 100):
#     print("Grade A")
# elif(marks>= 79 and marks<90):
#     print("Grade B")
# elif(marks >=69 and marks<79 ):
#     print("Grade C")
# elif(marks<69):
#     print("Grade F")
# else:
#     print("Invalid Marks")





# -----------------------------------------------

# List
# List is Collective Data type used to store more than 1 values

# mark1 = 89.9
# mark2 = 76.7
# mark3 = 23.4
# mark4 = 65.4
# mark5 = 54.5

# marks = [89.9, 76.7, 23.4, 65.4, 54.5]
# print(marks)
# print(type(marks))
# print(len(marks))


# We can create list of multiple datatypes
# student = ["Bilal", 86, "A"]
# print(student)


# indexing in List

# marks = [89.9, 76.7, 23.4, 65.4, 54.5]
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])


# We can change value of List using index
# marks[3] = 78.4

# print("marks 3",marks[3])


# Slicing
# marks = [89.9, 76.7, 23.4, 65.4, 54.5]
# print(marks[0:3])
# print(marks[1:])
# print(marks[:2])


# List Methods

# marks = [89.9, 76.7, 23.4, 65.4, 54.5]

# add value at the end
# marks.append(34.5)
# print("add",marks)

# sort list
# marks.sort()
# print("Sort",marks)

# # Sort in decending order
# marks.sort(reverse=True)
# print("Decending Sort",marks)

# Reverse List
# marks.reverse()
# print("Reverse",marks)

# # Insert value at index
# marks.insert(1,43.3)
# print("insert",marks)

# marks = [89.9, 76.7, 23.4, 65.4, 54.5]

# remove element
# marks.remove(23.4)
# print("Remove",marks)


# pop element at index
# marks.pop(1)
# print(marks)

# newMarks = marks.copy()
# print(newMarks)



# _------------------------------------------_

# Tuples
# Built in data type for immutable sequence of values


# tup = (2,3,4,5)
# print(tup)
# print(len(tup))
# print(type(tup))


# also have indexing
tup = (2,3,4,5)
# print(tup[0])
# print(tup[1])
# print(tup[2])

# does not allow this
# tup[0] = 23
# print(tup) #'tuple' object does not support item assignment

# Tuple Methods
tup = (2, 1, 3, 1)
print(tup.count(1))
print("index",tup.index(3)) # return the first index of the given number
 






