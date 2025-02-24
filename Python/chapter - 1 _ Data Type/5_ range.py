# Databricks notebook source
Range (range) – Sequence of numbers
•	A range generates a sequence of numbers, commonly used for looping in for loops. It is an iterable and can be defined by specifying a start, stop, and step.
Operations
 	 	 	 
Operation	Syntax	Example	Output
Iteration	for loop	for x in range(5): print(x)	0, 1, 2, 3, 4
Length	len()	len(range(10))	10
List Conversion	list()	list(range(3))	[0, 1, 2]


# COMMAND ----------

Syntax of range()
start (optional) – The beginning value (default: 0).
stop (required) – The end value (exclusive).
step (optional) – The increment (default: 1)

# COMMAND ----------

range(start, stop, step)

# COMMAND ----------

# Creating a Range
range1 = range(10)  # 0 to 9
range2 = range(5, 15)  # 5 to 14
range3 = range(0, 20, 2)  # Even numbers from 0 to 18

print("Range 1:", list(range1))
print("Range 2:", list(range2))
print("Range 3:", list(range3))

# COMMAND ----------

# type of Range Data Type
type(range1)

# COMMAND ----------

id(range1)

# COMMAND ----------

# Creating a Range
range_new = range(10)  # 0 to 9
id(range_new)

# COMMAND ----------

# Iterating Over a Range
for i in range(0, 20, 2):
    print("Iteration:", i)

# COMMAND ----------

# Checking Membership
print("Is 5 in range2?", 5 in range2)
print("Is 20 in range3?", 20 in range3)

# COMMAND ----------

# Using Range with List Slicing
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Elements at even indices:", [my_list[i] for i in range(0, len(my_list), 2)])

# COMMAND ----------

# Converting Range to List
range_list = list(range(1, 11))
print("Converted Range to List:", range_list)

# COMMAND ----------

# Using Range in Reverse Order
reverse_range = range(10, 0, -1)
print("Reverse Range:", list(reverse_range))

# COMMAND ----------

# Finding Min, Max, and Length
print("Min in range2:", min(range2))
print("Max in range2:", max(range2))
print("Length of range3:", len(range3))

# COMMAND ----------

#Key Properties of range
#It is immutable.
#It supports indexing and slicing.
#It does not store all values in memory but generates them dynamically.
#It is more memory-efficient than a list.