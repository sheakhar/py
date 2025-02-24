# Databricks notebook source
# MAGIC %md
# MAGIC • Tuple Operations in Python.
# MAGIC • A tuple is similar to a list but immutable (cannot be changed after creation)..
# MAGIC • Example: tuple1 = (1, 2, 3, 4, 5)
# MAGIC •	Supports indexing, slicing, searching, and concatenation.

# COMMAND ----------

# Creating a Tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apple", "banana", "cherry")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# COMMAND ----------

#type
type(tuple1)

# COMMAND ----------

# Creating a Tuple
tuple3 = (1, 2, 3, 4, 5)
id(tuple1)

# COMMAND ----------

tuple4 = (1, 2, 3, 4, 5, 6)
type(tuple4)
id(tuple4)

# COMMAND ----------

tuple5 = (1, 2, 3, 4, 5, 6)
type(tuple4)
id(tuple5)

# COMMAND ----------


id(tuple3)

# COMMAND ----------

# Accessing Elements
print("First Element:", tuple1[0])
print("Last Element:", tuple1[-1])

# COMMAND ----------

# Slicing a Tuple
print("Elements from index 1 to 3:", tuple1[1:4])
print("First three elements:", tuple1[:3])
print("Every second element:", tuple1[::2])

# COMMAND ----------

# Tuple Concatenation and Repetition
tuple3 = tuple1 + tuple2
print("Concatenated Tuple:", tuple3)
print("Repeated Tuple:", tuple1 * 2)

# COMMAND ----------

# Checking Membership
print("Is 2 in tuple1?", 2 in tuple1)
print("Is 'grape' not in tuple2?", "grape" not in tuple2)

# COMMAND ----------

# Looping Through a Tuple
for item in tuple1:
    print("Item:", item)

# COMMAND ----------

# Finding Length, Min, Max
print("Length of tuple1:", len(tuple1))
print("Max Element in tuple1:", max(tuple1))
print("Min Element in tuple1:", min(tuple1))

# COMMAND ----------

# Counting and Indexing
sample_tuple = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", sample_tuple.count(2))
print("Index of 3:", sample_tuple.index(3))

# COMMAND ----------

# Tuple Unpacking
a, b, c = (10, 20, 30)
print("Unpacked Values:", a, b, c)

# COMMAND ----------

# Nested Tuples
nested_tuple = ((1, 2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing Nested Element:", nested_tuple[1][2])