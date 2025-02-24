# Databricks notebook source
# MAGIC %md
# MAGIC 1.• A string is a sequence of characters.
# MAGIC • •	Immutable → Once created, it cannot be modified..
# MAGIC Example: my_string = "Hello, Databricks!"
# MAGIC ••	Supports indexing, slicing, searching, and concatenation..

# COMMAND ----------

# Creating a String
my_string = "Hello, Databricks!"
print("Original String:", my_string)

# COMMAND ----------

# Accessing Characters
print("First Character:", my_string[0])
print("Last Character:", my_string[-1])

# COMMAND ----------

# Slicing a String
print("First 5 Characters:", my_string[:5])
print("Last 5 Characters:", my_string[-5:])
print("Every Second Character:", my_string[::2])

# COMMAND ----------

# String Concatenation
str1 = "Hello"
str2 = "Databricks"
full_string = str1 + ", " + str2 + "!"
print("Concatenated String:", full_string)

# COMMAND ----------

# String Repetition
print("Repeated String:", str1 * 3)

# COMMAND ----------

# Checking Membership
print("Is 'Databricks' in the string?", "Databricks" in my_string)
print("Is 'Python' not in the string?", "Python" not in my_string)

# COMMAND ----------

# String Methods
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Title Case:", my_string.title())
print("Replaced String:", my_string.replace("Databricks", "Python"))

# COMMAND ----------

# Splitting and Joining
words = my_string.split()
print("Split Words:", words)
joined_string = "-".join(words)
print("Joined String:", joined_string)

# COMMAND ----------

# Stripping Whitespace
whitespace_string = "   Hello, Databricks!   "
print("Stripped String:", whitespace_string.strip())

# COMMAND ----------

# Finding and Counting Substrings
print("Index of 'Databricks':", my_string.find("Databricks"))
print("Count of 'l':", my_string.count("l"))

# COMMAND ----------

# String Formatting
name = "Shekhar"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)

# COMMAND ----------

# Looping Through a List
for item in my_list:
    print("Item:", item)

# COMMAND ----------

# List Comprehension
squared = [x**2 for x in my_list]
print("Squared List:", squared)

# COMMAND ----------

# Sorting and Reversing
nums = [5, 2, 9, 1, 7]
nums.sort()
print("Sorted List:", nums)
nums.reverse()
print("Reversed List:", nums)

# COMMAND ----------

# Finding Max, Min, and Sum
print("Max Element:", max(nums))
print("Min Element:", min(nums))
print("Sum of Elements:", sum(nums))

