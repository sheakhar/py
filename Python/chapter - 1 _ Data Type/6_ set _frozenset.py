# Databricks notebook source
# MAGIC %md
# MAGIC 5.                                     **Set Types**
# MAGIC set – Unordered collection of unique items
# MAGIC •	A set is a collection of unordered, non-duplicate items. Useful when you need to store a collection where uniqueness matters.
# MAGIC Operations
# MAGIC 	
# MAGIC Operation	Syntax	Example	Output	
# MAGIC Addition	.add()	s.add(4)	{1, 2, 3, 4}	
# MAGIC Removal	.remove()	s.remove(3)	{1, 2, 4}	
# MAGIC Length	len()	len(s)	3	
# MAGIC Membership Test	in	2 in s	TRUE	
# MAGIC
# MAGIC
# MAGIC                                   **frozenset – Immutable set**
# MAGIC •	A frozenset is an immutable version of a set. Once created, you cannot modify it (add or remove elements).
# MAGIC Operations
# MAGIC 	
# MAGIC Operation	Syntax	Example	Output	
# MAGIC Length	len()	len(frozenset([1, 2, 3]))	3	
# MAGIC Membership Test	in	2 in frozenset([1, 2, 3])	TRUE	
# MAGIC

# COMMAND ----------

# Creating Sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)

# COMMAND ----------

#type
type(set1)

# COMMAND ----------

# Adding and Removing Elements
set1.add(6)  # Adds an element
set1.remove(2)  # Removes an element
print("Set 1 after adding and removing elements:", set1)

# COMMAND ----------

# Set Operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)

# COMMAND ----------

# Checking Membership
print("Is 3 in set1?", 3 in set1)
print("Is 10 not in set2?", 10 not in set2)

# COMMAND ----------

# Iterating Over a Set
for item in set1:
    print("Item:", item)

# COMMAND ----------

# Finding Length of a Set
print("Length of set1:", len(set1))

# COMMAND ----------

# Copying a Set
set_copy = set1.copy()
print("Copied Set:", set_copy)

# COMMAND ----------

# Clearing a Set
set_copy.clear()
print("Cleared Set:", set_copy)

# COMMAND ----------

# Creating a Frozenset
frozen_set1 = frozenset([1, 2, 3, 4, 5])
frozen_set2 = frozenset([4, 5, 6, 7, 8])
print("Frozenset 1:", frozen_set1)
print("Frozenset 2:", frozen_set2)

# COMMAND ----------

#type
type(frozen)

# COMMAND ----------

# Set Operations (Union, Intersection, Difference, Symmetric Difference)
union_set = frozen_set1 | frozen_set2
intersection_set = frozen_set1 & frozen_set2
difference_set = frozen_set1 - frozen_set2
symmetric_difference_set = frozen_set1 ^ frozen_set2

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)

# COMMAND ----------

# Checking Membership
print("Is 3 in frozen_set1?", 3 in frozen_set1)
print("Is 10 not in frozen_set2?", 10 not in frozen_set2)

# COMMAND ----------

# Iterating Over a Frozenset
for item in frozen_set1:
    print("Item:", item)

# COMMAND ----------

# Finding Length of a Frozenset
print("Length of frozen_set1:", len(frozen_set1))

# COMMAND ----------

# Copying a Frozenset
frozen_copy = frozenset(frozen_set1)
print("Copied Frozenset:", frozen_copy)

# COMMAND ----------

# Attempting to Modify a Frozenset (Will Raise Error)
try:
    frozen_set1.add(6)
except AttributeError as e:
    print("Error:", e)

try:
    frozen_set1.remove(2)
except AttributeError as e:
    print("Error:", e)