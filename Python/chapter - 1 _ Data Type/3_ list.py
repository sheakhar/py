# Databricks notebook source
# MAGIC %md
# MAGIC 1. List Operations in Python
# MAGIC • A list is an ordered, mutable collection of elements.
# MAGIC Example: my_list = [1, 2, 3, 4, 5]
# MAGIC •Supports addition, deletion, searching, and modification.

# COMMAND ----------

# Creating a List
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# COMMAND ----------

#type
type(my_list)

# COMMAND ----------

#Loaction of list
id(my_list)

# COMMAND ----------

# Creating a List
my_list_new = [1, 2, 3, 4, 5]
#Loaction of list
id(my_list_new)

# COMMAND ----------

a=4
id(a)

# COMMAND ----------

b=4
id(b)

# COMMAND ----------

# Accessing Elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# COMMAND ----------

# Slicing a List
print("Elements from index 1 to 3:", my_list[1:4])
print("First three elements:", my_list[:3])
print("Every second element:", my_list[::2])

# COMMAND ----------

# Modifying a List
my_list[1] = 10
print("Modified List:", my_list)

# COMMAND ----------

# Adding Elements
my_list.append(6)
my_list.insert(2, 20)
print("List after appending and inserting:", my_list)

# COMMAND ----------

# Removing Elements
my_list.pop()  # Removes last element
my_list.pop(2) # Removes element at index 2
my_list.remove(10) # Removes first occurrence of 10
print("List after removing elements:", my_list)

# COMMAND ----------

# List Operations
a = [1, 2, 3]
b = [4, 5, 6]
print("Concatenation:", a + b)
print("Repetition:", a * 2)

# COMMAND ----------

# Checking Membership
print("Is 2 in the list?", 2 in my_list)
print("Is 10 not in the list?", 10 not in my_list)

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

