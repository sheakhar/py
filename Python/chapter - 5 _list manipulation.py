# Databricks notebook source
# 5. List Manipulation in Python
# This notebook covers various list manipulation techniques in Python,
# including list creation, indexing, slicing, comprehensions, and common operations like sorting and filtering.
# We will explore advanced functionalities such as mapping, reducing, and using built-in functions effectively.

# COMMAND ----------

# 1. Creating and Initializing Lists
# Example: Different ways to create and initialize lists.

# Direct initialization
my_list = [1, 2, 3, 4, 5]
print(my_list)

# List comprehension
comprehension_list = [x**2 for x in range(6)]
print(comprehension_list)

# Using the list constructor
constructor_list = list("hello")
print(constructor_list)

# COMMAND ----------

# 2. Indexing and Slicing
# Example: Accessing elements using indices and slicing.

my_list = [10, 20, 30, 40, 50]

# Access by index
first_element = my_list[0]
print(first_element)

# Negative indexing
last_element = my_list[-1]
print(last_element)

# Slicing
sub_list = my_list[1:4]
print(sub_list)

# COMMAND ----------

# 3. List Comprehensions
# Example: Creating lists with comprehensions.

# Generating squares of even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Flattening a list of lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

# COMMAND ----------

# 4. Common List Operations
# Example: Basic list operations like append, extend, and remove.

# Initialize the list
fruits = ['apple', 'banana', 'cherry']

# Append a single item
fruits.append('orange')
print(fruits)

# Extend the list with another list
fruits.extend(['mango', 'grape'])
print(fruits)

# Remove an item
fruits.remove('banana')
print(fruits)

# COMMAND ----------

# 5. Sorting and Reversing
# Example: Sort and reverse a list.

numbers = [5, 2, 9, 1, 5, 6]

# Sort the list
numbers_sorted = sorted(numbers)
print(numbers_sorted)

# In-place sort (alters the original list)
numbers.sort()
print(numbers)

# Reverse the list
numbers.reverse()
print(numbers)

# COMMAND ----------

# 6. Filtering and Mapping
# Example: Using filter() and map() functions.

# Filter: Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Map: Double each number
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# COMMAND ----------

# 7. Reducing Lists
# Example: Summing elements using reduce().

from functools import reduce

# Sum all elements
total = reduce(lambda x, y: x + y, numbers)
print(total)

# COMMAND ----------

# 8. List Operations with Conditions
# Example: Conditional operations on lists.

# Check if all numbers are positive
all_positive = all(x > 0 for x in numbers)
print(all_positive)

# Check if any numbers are negative
any_negative = any(x < 0 for x in numbers)
print(any_negative)

# COMMAND ----------

# 9. Advanced List Techniques
# Example: Zip and enumerate.

# Using zip to combine lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(zip(list1, list2))
print(combined)

# Enumerate to access index and value
for index, value in enumerate(combined):
    print(f"Index: {index}, Value: {value}")

# COMMAND ----------

# 10. Questions and Solutions: Advanced List Manipulation Techniques

# 10.1 Flattening Deeply Nested Lists
# Description: Flatten a list of lists using recursion.

def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

# Example usage:
deeply_nested_list = [1, [2, [3, [4, 5]]], 6]
print(flatten_list(deeply_nested_list))

# COMMAND ----------

# 10.2 Removing Duplicates
# Description: Remove duplicates from a list without using set.

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
duplicated_list = [1, 2, 3, 2, 1, 4, 5]
print(remove_duplicates(duplicated_list))

# COMMAND ----------

# 10.3 Grouping Elements
# Description: Group elements by a criterion (e.g., even vs. odd).

from collections import defaultdict

def group_by_parity(lst):
    grouped = defaultdict(list)
    for num in lst:
        group_key = 'even' if num % 2 == 0 else 'odd'
        grouped[group_key].append(num)
    return dict(grouped)

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(group_by_parity(numbers_list))

# COMMAND ----------

# 10.4 Finding Max Product Pair
# Description: Find the pair of numbers with the maximum product.

def max_product_pair(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return max(lst[0] * lst[1], lst[-1] * lst[-2])

# Example usage:
numbers_for_product = [-10, -20, 5, 1]
print(max_product_pair(numbers_for_product))

# COMMAND ----------

# 10.5 Rotate a List
# Description: Rotate a list by k elements.

def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handles cases where k > n
    return lst[-k:] + lst[:-k]

# Example usage:
rotatable_list = [1, 2, 3, 4, 5]
print(rotate_list(rotatable_list, 2))

# COMMAND ----------

# These sections cover a wide range of list manipulation techniques suitable for someone with several years of experience with Python.
# You can adapt and expand each section based on specific requirements or to dive deeper into more complex functionalities.