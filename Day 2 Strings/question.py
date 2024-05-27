# String Question

# Q1: WAP to input user’s first name & print its length.

# inp = input("Enter your first name: ")
# print("Your name is",inp,"and length is",len(inp))

# Q2: WAP to find the occurrence of ‘$’ in a String.
# dummy = "$ work fine but $ is too short"
# freq = dummy.count('$')
# print("Frquency of $" ,freq)


# ----------------------------

# Conditionals
# Q1: WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter your Number"))
# if(num%2 == 0):
#     print("Even")
# else:
#     print("Odd")


# Q2: WAP to find the greatest of 3 numbers entered by the user.

# num1 = int(input("Enter your Number1: "))
# num2 = int(input("Enter your Number2: "))
# num3 = int(input("Enter your Number3: "))


# if(num1 > num2 and num1 > num3):
#     print("Num1 is greater",num1)
# elif(num2 > num3 and num2 > num1):
#     print("Num2 is greater",num2)
# else:
#     print("Num3 is greater",num3)



# Q3: WAP to check if a number is a multiple of 7 or not.Apna College

# num = int(input("Enter your Number: "))
# if(num % 7 == 0 ):
#     print(num,"is multiple of 7")
# else:
#     print(num,"is not multiple of 7")


# ----------------------------------------------
# List and Tuples


# WAP to ask the user to enter names of their 3 favorite movies
#  & store them in a list.

# movies = [];
# favMovie = input("Enter your Favourite Movie: ")
# movies.append(favMovie)
# favMovie = input("Enter your Favourite Movie: ")
# movies.append(favMovie)
# favMovie = input("Enter your Favourite Movie: ")
# movies.append(favMovie)

# print(movies)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1][1, “abc”, “abc”, 1]Apna College

# list = [1, 2, 3, 2, 1]
# newList = list.copy()
# newList.reverse()

# # print(list)
# # print(newList)

# if(list == newList):
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# WAP to count the number of students with the “A” grade in the following tuple.

# grades = ('C', 'D', 'A', "A", 'B', 'B', 'A')
          
# print("Count of A Grade is: ", grades.count("A"))  

# Store the above values in a list & sort them from “A” to “D”.
# [”C”, “D”, “A”, “A”, “B”, “B”, “A”]

# grades = ['C', 'D', 'A', "A", 'B', 'B', 'A']

# grades.sort()
# print(grades)










