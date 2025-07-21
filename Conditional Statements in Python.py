# #------------------Introduction------------------
# print("Hello, World!")

# #------------------Input and Output------------------
# name = input("Enter your name: ")
# print("Welcome", name)

# #------------------Variables---------------------------

# age = 25
# name = "Alice"
# pi = 3.14
# print(name, "is", age, "years old.")

#-------------------------swapping-------------------
# x = 100
# y = 200

# # Pythonic swapping
# x, y = y, x
# x = 100
# y = 200

# # Using a temporary variable
# temp = x  # Store x's value in temp
# x = y     # Assign y's value to x
# y = temp  # Assign temp's value to y

#------------------ id() function-----------------------------

# print(id(5))  # Unique identifier for the object with value 5
# a = 10
# print(id(a))  # Unique identifier for the object with value 10
# b = a
# print(id(b))  # Same identifier as a because both refer to the same object

#------------------------------type() function--------------------------

# b = 10.5
# print(type(b))	# Output: <class 'float'>


# #------------------Operators---------------------------

# a = 10
# b = 3

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)

#--------------------Arithmetic Operators------------------
# a = 2
# b = 3

# # using the addition operator
# res = a + b
# print(res)

#--------------------------logical operators--------------

# a = 10
# b = 20
# c = 30

# print(a < b and b < c)  	# Output: True
# print(a < b or b > c)   	# Output: True
# print(not a > b)         	# Output: True

#--------------------identity operators-------------------

# x1 = 10
# x2 = 10
# y1 = 10.5
# y2 = 10.5
# z1 = "geeksforgeeks"
# z2 = "geeksforgeeks"

# print(x1 is x2)	# Output: True
# print(y1 is y2)	# Output: True
# print(z1 is z2)	# Output: True


#------------------Keywords------------------

# Keywords are reserved words in Python

# # def, return, if, else are keywords
# def say_hello():
#     return "Hello"

#------------------Data Types------------------

# a = 10           # int
# b = 5.5          # float
# c = "Python"     # string
# d = True         # boolean

# print(type(a), type(b), type(c), type(d))

# #---------------Nested if..else Conditional Statements-----------------

# # is_raining = True
# # has_umbrella = False

# # if is_raining:
# #     if has_umbrella:
# #         print("Go outside with your umbrella.")
# #     else:
# #         print("Stay inside, no umbrella!")
# # else:
# #     print("Enjoy the day outside!")

# #----------------Ternary Conditional Statement----------------

# # age = 18
# # status = "Adult" if age >= 18 else "Minor"
# # print(status)

# #--------------Match-Case Statement in Python------------------

# # day = "Thursday"

# # match day:
# #     case "Monday":
# #         print("Start of the work week.")
# #     case "Friday":
# #         print("Almost weekend!")
# #     case "Sunday":
# #         print("Time to relax.")
# #     case _:
# #         print("Just another day.")


# #------------------Python Loops------------------# For loop
# for i in range(3):
#     print("Loop index:", i)

# # While loop
# count = 0
# while count < 2:
#     print("Count is:", count)
#     count += 1

# #------------------Strings------------------
# s = "python"

# print(s.upper())
# print(s[0])        # First letter
# print(len(s))      # Length of string

# #------------------List------------------

# fruits = ["apple", "banana"]
# fruits.append("cherry")
# print(fruits)
# print(fruits[1])  # Access second item

# #------------------Tuples------------------

# t = (1, 2, 3)
# print(t[0])
# # Tuples are immutable

# #------------------Dictionary------------------------
# person = {"name": "Alice", "age": 25}
# print(person["name"])

# #------------------Set-------------------------------
# nums = {1, 2, 2, 3}
# print(nums)  # Output: {1, 2, 3}

# #------------------Array----------------------
# import array
# arr = array.array('i', [1, 2, 3])
# print(arr[0])

#------------------------------Geometric Progression (GP)--------------------------
# Program to calculate nth term of a geometric progression

# Input the first term (a)
a = 5000  	# First term
r = 2  		# Common ratio
n = 11    	# Term number

# Calculate the nth term using the formula
# nth_term = a * (r ** (n - 1))

# Print the result
# print("The 11th term of the geometric progression is: ", nth_term)

#------------------------------





