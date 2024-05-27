# Day 2 of 7 Days Python Challenge

<img src="./Day 02 of Python Challenge.png">

## Topics Covered

### Strings and Methods

Strings are sequences of characters. Python provides various methods to manipulate strings, such as `lower()`, `upper()`, `strip()`, `replace()`, and `split()`.

### Lists and Methods

Lists are ordered collections of items. Lists are mutable, meaning their elements can be changed. Common methods include `append()`, `remove()`, `pop()`, `sort()`, and `reverse()`.

### Tuples and Methods

Tuples are ordered collections of items, similar to lists, but they are immutable, meaning their elements cannot be changed. Common methods include `count()` and `index()`.

### Conditional Statements

Conditional statements allow you to execute different blocks of code based on certain conditions. The main conditional statements in Python are `if`, `elif`, and `else`.

## Learning Outcomes

- Understood how to work with strings and various string methods.
- Learned how to create, modify, and manipulate lists using list methods.
- Understood the properties of tuples and how to use tuple methods.
- Implemented conditional statements to control the flow of the program based on conditions.

## Practice Questions

### Strings and Methods

1. Write a Python program to convert a string to lowercase.
2. Write a program that replaces all occurrences of a substring within a string with another substring.
3. Create a program that takes a string and splits it into a list of words.
4. Write a program to find the length of a string.
5. Create a program that checks if a string starts with a specific substring.

### Lists and Methods

6. Write a Python program to create a list of integers and print it.
7. Write a program that appends a new item to a list.
8. Create a program that sorts a list of numbers in ascending order.
9. Write a program to remove an item from a list by value.
10. Create a program that reverses the elements of a list.

### Tuples and Methods

11. Write a Python program to create a tuple and print it.
12. Write a program that finds the index of a specific element in a tuple.
13. Create a program that counts the occurrences of a specific element in a tuple.
14. Write a program to convert a list to a tuple.
15. Create a program that checks if an element exists within a tuple.

### Conditional Statements

16. Write a Python program that checks if a number is positive, negative, or zero.
17. Create a program that determines if a person is eligible to vote based on their age.
18. Write a program that finds the largest of three numbers using conditional statements.
19. Create a program that checks if a string is empty and prints an appropriate message.
20. Write a program that prints "Pass" if a student's score is 50 or more, and "Fail" otherwise.

## Code Examples

### Strings and Methods

```python
# Convert string to lowercase
text = "Hello World"
print(text.lower())

# Replace substring
text = "Hello World"
print(text.replace("World", "Python"))

# Split string into words
text = "Hello World"
print(text.split())

# Find length of string
text = "Hello World"
print(len(text))

# Check if string starts with a substring
text = "Hello World"
print(text.startswith("Hello"))
```

### Lists and Methods

```
# Create and print list
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Append item to list
numbers.append(6)
print(numbers)

# Sort list
numbers.sort()
print(numbers)

# Remove item from list
numbers.remove(3)
print(numbers)

# Reverse list
numbers.reverse()
print(numbers)
```

### Tuples and Methods

```
# Create and print tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Find index of element
print(my_tuple.index(3))

# Count occurrences of element
print(my_tuple.count(3))

# Convert list to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

# Check if element exists in tuple
print(3 in my_tuple)
```

### Conditional Statements

```
# Check if number is positive, negative, or zero
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Check if eligible to vote
age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Find largest of three numbers
a, b, c = 10, 20, 30
if a > b and a > c:
    print("a is the largest")
elif b > a and b > c:
    print("b is the largest")
else:
    print("c is the largest")

# Check if string is empty
text = ""
if not text:
    print("String is empty")
else:
    print("String is not empty")

# Check pass or fail
score = 75
if score >= 50:
    print("Pass")
else:
    print("Fail")

```

Repository Link
Follow my progress and check out my code on my GitHub: https://github.com/Muhammad-Bilal01/7-days-python-challenge
