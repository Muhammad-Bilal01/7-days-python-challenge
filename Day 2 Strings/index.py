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

marks = int(input("Enter your Marks: "))

if(marks >= 90 and marks <= 100):
    print("Grade A")
elif(marks>= 79 and marks<90):
    print("Grade B")
elif(marks >=69 and marks<79 ):
    print("Grade C")
elif(marks<69):
    print("Grade F")
else:
    print("Invalid Marks")








