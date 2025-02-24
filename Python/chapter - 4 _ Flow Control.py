# Databricks notebook source
# 1. Flow Control in Python
# This section explains how to control the execution flow of your program using conditional statements, loops, and control flow modifiers.

# COMMAND ----------

# 1.1 Conditional Statements
# Conditional statements execute specific blocks of code based on whether conditions are True or False.

# COMMAND ----------

# 1.1.1 if Statement
# Executes a block of code only if the condition is True.

age = 20
if age >= 18:
    print("You are eligible to vote.")  # Output: You are eligible to vote.

# COMMAND ----------

# 1.1.2 if-else Statement
# Provides an alternative block of code if the condition is False.

temperature = 25
if temperature > 30:
    print("It's hot outside.")
else:
    print("The weather is pleasant.")  # Output: The weather is pleasant.

# COMMAND ----------

# 1.1.3 if-elif-else Ladder
# Used when multiple conditions need to be checked.

marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")  # Output: Grade B
else:
    print("Grade C")

# COMMAND ----------

# 1.1.4 Nested if Statements
# Allows more complex decision-making with multiple layers of conditions.

age = 13
has_id = True

if age >= 18:
    if has_id:
        print("You are allowed entry.")  # Output: You are allowed entry.
    else:
        print("ID required for entry.")

# COMMAND ----------

# 2. Loops
# Loops allow repetitive execution of a block of code.

# COMMAND ----------

# 2.1 for Loop
# Iterates over sequences like lists, tuples, and strings.

# Iterating over a range of numbers
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit , exit(" "))  # Output: apple, banana, cherry

# COMMAND ----------

# 2.2 while Loop
# Executes a block of code as long as the condition remains True.

count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1

# COMMAND ----------

# 3. Control Flow Statements
# Modify the behavior of loops and conditionals.

# COMMAND ----------

# 3.1 break Statement
# Terminates the loop immediately when the condition is met.

for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0, 1, 2, 3, 4

# COMMAND ----------

# 3.2 continue Statement
# Skips the current iteration and moves to the next.

for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4

# COMMAND ----------

3
2
1
0
-1

# COMMAND ----------

# 3.3 pass Statement
# A placeholder for future code, does nothing.

for i in range(5):
    if i == 3:
        pass  # Placeholder
    print(i)  # Output: 0, 1, 2, 3, 4

# COMMAND ----------

# 4. Loop else Clause
# Executes if the loop completes normally (not terminated by break).

for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break.")  # Output: Loop completed without break.

# COMMAND ----------

# 5. Nested Loops
# A loop inside another loop to handle complex data structures.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # New line after each row

# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9

# COMMAND ----------

# 6. More Examples of Nested Loops and Flow Control

# Nested loops with a pattern printing example
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# Using break inside a nested loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"({i}, {j})", end=" ")
    print()
# Output:
# (0, 0) (0, 1)
# (1, 0) (1, 1)
# (2, 0) (2, 1)

# Using continue inside a nested loop
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"({i}, {j})", end=" ")
    print()
# Output:
# (0, 0) (0, 2)
# (1, 0) (1, 2)
# (2, 0) (2, 2)

# COMMAND ----------

# End of Notebook
# This notebook covered detailed flow control structures in Python, including conditionals, loops, control flow modifiers, and nested loops for efficient programming.