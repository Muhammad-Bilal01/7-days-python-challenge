# print("Hello Python")

# Print Multiple vales 
# print("My name is Muhammad Bilal","My Age is 21")
# python automatically seperate it by sigle white space

# Variable in Python
# memory location to store some values

# a = 10
# b = 20.4
# name = "Bilal"
# isRight = True

# print(a)
# print(b)
# print(name)
# print(isRight)

# DataTypes
# 5 - Major Data types
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean
# 5. None

# We can find type of any value with type() method

# a = 12
# b = 23.4
# name = "bilal"
# isComplete = True
# hasData = None


# print("a type: ",type(a)," Value ",a)
# print("b type: ",type(b)," Value ",b)
# print("name type: ",type(name)," Value ",name)
# print("is Complete type: ",type(isComplete)," Value ",isComplete)
# print("hasData type: ",type(hasData)," Value ",hasData)

# ---------------------
# Type Casting and Type Conversion

# Type Convertion: Convertion of Type by python automaticaaly

# chote type ko baare type me convert kr diya

# a = 10 # int
# b = 23.5 # float
# sum = a + b # int + float = float
# print("a + b = ",sum," and type of sum is ",type(sum))

# Type Convertion: Forcefully Type Convertion

# Bare type ko chote type me convert krna

# a = "10" # str
#  ERROR: sum = a + b # int + float = float

# a = int("10") # typecast str to int
# b = 23.5 # float
# sum = a + b # int + float = float
# print("a + b = ",sum," and type of sum is ",type(sum)) 

# we can type cast any of the value

# a = int("20")
# b = float("23.5")
# print(a+b)


# Comments

# 1. Single Line Comment
# 2. Multiline Comment
# used for function documentation
""""
Multi
line 
Comment
"""

# Operators

# # Arithmetic Operator
# a = 10
# b = 20

# print("-"*8,"Arithmetic Operator","-"*8)

# print("Sum", a+b)
# print("Diff", a-b)
# print("Multiply", a*b)
# print("Power", a**b)
# print("Divide", a/b)
# print("Integer Divide", a//b)
# print("Modules", a%b)

# Relational / Comparision Operator
# a = 10
# b = 20

# print("-"*8,"Relational Operator","-"*8)

# print("Equals", a==b)
# print("Not Equals", a!=b)
# print("greater", a>b)
# print("less than", a<b)
# print("Less equals to", a<=b)

# Assignment Operator
# (=, +=, -=, *=, /=, %=, **=)

# Logical Operator
# only working on boolean values or expression that return booleans values

# a = 10
# b = 20

# print("-"*8,"Logical Operator","-"*8)

# AND Operator
# print("AND Operator")
# print(True and True)
# print(True and False)
# print(False and False)
# print(False and True)

# OR Operator
# print() # just for line space

# print("OR Operator")
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)


# NOT Operator
# print() # just for line space

# print("NOT Operator")
# print( not True)
# print(not False)


# INPUT
# always return String value
# a = input("Enter Value ")
# print(a , type(a))

# We can use typecasting for convestion of this type
# name = input("Enter Your name: ")
# age = int(input("Enter Your age: "))

# print("Name :",name,type(name))
# print("Age :",age,type(age))


# Question

# Write a program to get two number from user and print their sum
a = int(input("Enter 1st No: "))
b = int(input("Enter 2nd No: "))

print("a + b =",a+b)



