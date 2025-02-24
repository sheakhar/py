# Databricks notebook source
# MAGIC %md
# MAGIC Boolean Type Representation
# MAGIC
# MAGIC The bool type in Python has two values: True and False.
# MAGIC It is a subclass of the integer type (int), meaning True is equivalent to 1 and False is equivalent to 0.
# MAGIC Immutable
# MAGIC
# MAGIC Once a boolean value is created, it cannot be modified.
# MAGIC Boolean as Numbers
# MAGIC
# MAGIC True behaves like 1, and False behaves like 0 in arithmetic operations.
# MAGIC

# COMMAND ----------

# Boolean Values
bool_true = True
bool_false = False
print("Boolean True:", bool_true)
print("Boolean False:", bool_false)

# COMMAND ----------

type(True)

# COMMAND ----------

# Boolean from Expressions
print("5 > 3:", 5 > 3)
print("10 == 20:", 10 == 20)
print("7 <= 7:", 7 <= 7)

# COMMAND ----------

# Boolean with Logical Operators
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# COMMAND ----------

# Boolean with Comparisons
x, y = 10, 20
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= 10 and y <= 20:", x >= 10 and y <= 20)

# COMMAND ----------

# Boolean with Collections
empty_list = []
non_empty_list = [1, 2, 3]
print("Is empty list False?:", bool(empty_list))
print("Is non-empty list True?:", bool(non_empty_list))

# COMMAND ----------

6 * False

# COMMAND ----------

True + True + True +3 

# COMMAND ----------

# Boolean Conversion
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(None):", bool(None))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))

# COMMAND ----------

# Using Booleans in Conditional Statements
if bool_true:
    print("This will execute because bool_true is True")

if not bool_false:
    print("This will execute because bool_false is False")