# Databricks notebook source
# 1. Input and Output in Python
# This section explains how to handle basic input and output operations in Python.

# COMMAND ----------

# 1.1 Output using print()
# The print() function is used to display information to the console.

# Simple string output
print("Hello, World!")  # Output: Hello, World!

# Output with multiple arguments
name = "Shekhar"
age = 30
print("Name:", name, "Age:", age)  # Output: Name: Shekhar Age: 30

# Using formatted strings (f-strings)
print(f"Name: {name}, Age: {age}")  # Output: Name: Shekhar, Age: 30

# Using escape characters
print("Shekhar\nSuman")  # Output: Shekhar (new line) Suman

# COMMAND ----------

# 1.2 Input using input()
# The input() function allows you to take input from the user. Input is always read as a string.

# Taking a simple string input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Taking numeric input and converting to integer
user_age = int(input("Enter your age: "))
print(f"You are {user_age} years old.")

# Taking float input
user_salary = float(input("Enter your salary: "))
print(f"Your salary is {user_salary}")

# COMMAND ----------

# 2. Advanced Input and Output
# This section covers more advanced techniques for handling input and output.

# COMMAND ----------

# 2.1 Reading Multiple Inputs
# You can take multiple inputs in one line and split them.

# Example: Reading two numbers separated by space
a, b = input("Enter two numbers separated by comma: ").split(",")
print(f"First Number: {a}, Second Number: {b}")

# Converting to integers
a, b = map(int, input("Enter two numbers: ").split())
print(f"Sum: {a + b}")

# Reading multiple inputs into a list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Numbers List: {numbers}")

# COMMAND ----------

# 2.2 Using split() Function
# The split() method splits a string into a list where each word is a list item.

# Example: Splitting a sentence into words
sentence = "Python is a powerful language"
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'a', 'powerful', 'language']

# Example: Splitting by a specific delimiter
data = "apple,banana,grape"
fruits = data.split(",")
print(fruits)  # Output: ['apple', 'banana', 'grape']

# Limiting the number of splits
limited_split = sentence.split(" ", 2)
print(limited_split)  # Output: ['Python', 'is', 'a powerful language']

# COMMAND ----------

# 3. Formatting Output
# Python provides various ways to format output for better readability.

# COMMAND ----------

# 3.1 Using format() Method
# The format() method allows you to insert variables into strings.

name = "Nidhi"
age = 28
print("Name: {}, Age: {}".format(name, age))  # Output: Name: Nidhi, Age: 28

# Using positional and keyword arguments
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# COMMAND ----------

# 3.2 Using f-strings (Python 3.6+)
# F-strings provide a more readable and concise way to format strings.

salary = 75000.50
print(f"Employee: {name}, Age: {age}, Salary: ${salary:.2f}")  # Output: Employee: Nidhi, Age: 28, Salary: $75000.50

# Embedding expressions inside f-strings
print(f"Next year, {name} will be {age + 1} years old.")

# COMMAND ----------

# 4. Error Handling in Input
# This section covers how to handle errors during input.

# COMMAND ----------

# 4.1 Handling ValueError during numeric input
try:
    user_age = int(input("Enter your age: "))
    print(f"Your age is {user_age}")
except ValueError:
    print("Invalid input! Please enter a number.")

# Handling multiple exceptions
try:
    user_number = int(input("Enter a number: "))
    result = 10 / user_number
    print(f"Result is {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# COMMAND ----------

# 5. Using eval() Function
# The eval() function parses and evaluates a string as a Python expression.

# Example: Evaluating a simple arithmetic expression
expression = input("Enter an arithmetic expression (e.g., 2 + 3 * 4): ")
result = eval(expression)
print(f"Result: {result}")

# Evaluating list operations
list_expression = input("Enter a list operation (e.g., [1,2,3] + [4,5]): ")
list_result = eval(list_expression)
print(f"List Result: {list_result}")

# Caution: Be careful when using eval() with untrusted input as it can execute arbitrary code.

# COMMAND ----------

# 6. Additional Features
# This section covers more Python input/output features that are useful for professionals.

# 6.1 Using json for structured data
import json

# Writing JSON to a file
data = {"name": "Shekhar", "age": 30, "city": "Patna"}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON from a file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)

# 6.2 Using sys for advanced output
import sys

# Writing to standard error
print("This is an error message", file=sys.stderr)

# Redirecting output to a file
with open("log.txt", "w") as log_file:
    print("Logging information...", file=log_file)