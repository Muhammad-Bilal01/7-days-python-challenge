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

num = int(input("Enter your Number: "))
if(num % 7 == 0 ):
    print(num,"is multiple of 7")
else:
    print(num,"is not multiple of 7")
