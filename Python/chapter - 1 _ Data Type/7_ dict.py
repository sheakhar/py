# Databricks notebook source
# Creating a Dictionary
my_dict = {"name": "Shekhar", "age": 30, "city": "Patna"}
print("Dictionary:", my_dict)

# COMMAND ----------

# Accessing Values
print("Name:", my_dict["name"])
print("Age:", my_dict.get("age"))

# COMMAND ----------

# Adding and Updating Elements
my_dict["profession"] = "Data Engineer"
my_dict["age"] = 31
print("Updated Dictionary:", my_dict)

# COMMAND ----------

# Removing Elements
del my_dict["city"]
age = my_dict.pop("age")
print("Dictionary after removal:", my_dict)
print("Removed Age:", age)

# COMMAND ----------

# Dictionary Keys, Values, and Items
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# COMMAND ----------

# Iterating Through a Dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# COMMAND ----------

# Checking Membership
print("Is 'name' a key in my_dict?", "name" in my_dict)
print("Is 'city' not in my_dict?", "city" not in my_dict)

# COMMAND ----------

dict3=dict1|dict2
print(dict3)

# COMMAND ----------

# Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print("Merged Dictionary:", dict1)

# COMMAND ----------

# Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}
print("Squared Dictionary:", squared_dict)

# COMMAND ----------

# Copying a Dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# COMMAND ----------

# Clearing a Dictionary
copied_dict.clear()
print("Cleared Dictionary:", copied_dict)

