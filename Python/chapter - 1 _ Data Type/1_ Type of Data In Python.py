# Databricks notebook source
# MAGIC %md
# MAGIC 1. Integer (int)
# MAGIC Whole numbers, positive or negative, without decimal points.
# MAGIC Example: 10, -5, 1000
# MAGIC Python automatically supports large integers without overflow.
# MAGIC Associated Functions
# MAGIC abs(x) → Absolute value

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Integer (int)
# MAGIC Whole numbers, positive or negative, without decimal points.
# MAGIC Example: 10, -5, 1000
# MAGIC Python automatically supports large integers without overflow.
# MAGIC #### Associated Functions
# MAGIC - **abs(x)** → Absolute value
# MAGIC - **pow(base, exp, mod)** → Exponentiation with optional modulus
# MAGIC - **bin(x), oct(x), hex(x)** → Convert to binary, octal, hexadecimal

# COMMAND ----------

b=1.3
type(b)

# COMMAND ----------

# Integer Functions
print(abs(-10))  # Output: 10
print(pow(2, 3))      # Output: 8 (2^3)
print(pow(2, 3, 5))   # Output: 3 (2^3 % 5)
print(bin(10))   # Output: '0b1010' (binary)
print(oct(10))   # Output: '0o12'  (octal)
print(hex(10))   # Output: '0xa'   (hexadecimal)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Floating-Point (float)
# MAGIC Numbers with a decimal point or in scientific notation.
# MAGIC Example: 3.14, -0.01, 1.2e3 (1200.0)
# MAGIC #### Associated Functions
# MAGIC - **round(x, n)** → Round to n decimal places
# MAGIC - **int(x)** → Convert float to integer (truncates decimal part)
# MAGIC - **float(x)** → Convert int or string to float
# MAGIC - **math.ceil(x), math.floor(x)** → Round up/down
# MAGIC - **math.sqrt(x)** → Square root

# COMMAND ----------

import math
print(round(3.14159, 2))  # Output: 3.14
print(int(5.99))  # Output: 5
print(float(10))   # Output: 10.0
print(float("3.14"))  # Output: 3.14
print(math.ceil(2.3))   # Output: 3
print(math.floor(2.7))  # Output: 2
print(math.sqrt(16))  # Output: 4.0

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Complex Number (complex)
# MAGIC Complex numbers have a real and imaginary part, written as a + bj where j is the imaginary unit (√-1).
# MAGIC Example: 3 + 4j, 2 - 3j
# MAGIC #### Associated Functions
# MAGIC - **Creating a complex number**
# MAGIC - **Accessing real and imaginary parts**
# MAGIC - **abs(x)** → Magnitude of complex number
# MAGIC - **cmath module** for complex math

# COMMAND ----------

import cmath
z = complex(3, 4)  # 3 + 4j
print(z)  # Output: (3+4j)
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0
print(abs(3 + 4j))  # Output: 5.0 (since √(3² + 4²) = 5)
print(cmath.sqrt(-1))  # Output: 1j
print(cmath.exp(1j))   # Euler's formula

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sequence Types in Python
# MAGIC ### 1. String (str) – Immutable
# MAGIC A string is a sequence of characters. Supports indexing, slicing, searching, and concatenation.

# COMMAND ----------

s1 = "Hello, World"
s2 = 'Python'
s3 = """Multiline
string"""
print(s1, s2, s3)

# COMMAND ----------

s = "Hello"
s = s + " World"  # New string is created
print(s)  # Output: "Hello World"

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. List (list) – Mutable
# MAGIC A list is an ordered, mutable collection of elements.

# COMMAND ----------

lst = [10, 20, 30, 40]
lst.append(50)
lst.insert(1, 15)
lst.remove(30)
print(lst)  # Output: [10, 15, 20, 40, 50]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Tuple (tuple) – Immutable
# MAGIC A tuple is similar to a list but immutable.

# COMMAND ----------

tup = (10, 20, 30, 40)
tup_concat = tup + (50, 60)
tup_slice = tup[1:3]
print(tup_concat)  # Output: (10, 20, 30, 40, 50, 60)
print(tup_slice)  # Output: (20, 30)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Common Sequence Operations

# COMMAND ----------

# Indexing
s = "Python"
l = [10, 20, 30]
t = (100, 200, 300)
print(s[2], l[0], t[-1])

# COMMAND ----------

# Slicing
print(s[1:4])
print(s[:3])
print(s[::3])

# COMMAND ----------

# Concatenation
print([1, 2] + [3, 4])
print("Hello " + "World")
print((1, 2) + (3, 4))

# COMMAND ----------

# Repetition
print("A" * 3)
print([1, 2] * 2)
print((10, 20) * 3)

# COMMAND ----------

# Membership
print(10 in [10, 20, 30])
print("a" in "apple")
print(50 not in (10, 20))

# COMMAND ----------

# Iteration
for char in "Python":
    print(char, end=" ")

# COMMAND ----------

# Length
print(len([1, 2, 3]))
print(len("Python "))

# COMMAND ----------

# Min & Max
print(min([3, 1, 5]))
print(max("abcde"))

# COMMAND ----------

# Count & Index
lst = [10, 20, 10, 30]
print(lst.count(20))
print(lst.index(30))

# COMMAND ----------

# Sorting & Reversing
print(sorted([3, 1, 4, 2]))
print(list(reversed("Python")))

%md
## Range (range)
The `range` type represents an immutable sequence of numbers commonly used in loops.

### Syntax:
```python
range(start, stop, step)
```
- `start` (optional): The starting number (default is 0).
- `stop`: The number before which the sequence stops.
- `step` (optional): The increment (default is 1).

# COMMAND ----------

# Creating range objects
r1 = range(5)       # 0, 1, 2, 3, 4
r2 = range(1, 10, 2) # 1, 3, 5, 7, 9

# Converting range to list
print(list(r1))  # Output: [0, 1, 2, 3, 4]
print(list(r2))  # Output: [1, 3, 5, 7, 9]

# Iterating over a range
for num in range(3):
    print(num, end=' ')  # Output: 0 1 2

# COMMAND ----------

# MAGIC %md
# MAGIC ## Set (set)
# MAGIC A `set` is an unordered collection of unique elements.
# MAGIC - **Mutable**: You can add or remove elements.
# MAGIC - **Unordered**: No specific order is maintained.
# MAGIC - **Unique Elements**: Duplicates are not allowed.

# COMMAND ----------

# Creating sets
s1 = {1, 2, 3, 4, 5}
s2 = set([3, 4, 5, 6])  # Using set() constructor

print(s1)  # Output: {1, 2, 3, 4, 5}
print(s2)  # Output: {3, 4, 5, 6}

# Adding elements
s1.add(10)
print(s1)  # Output: {1, 2, 3, 4, 5, 10}

# Removing elements
s1.remove(2)  # Removes 2
print(s1)  # Output: {1, 3, 4, 5, 10}

# Set operations
print(s1.union(s2))   # Union: {1, 3, 4, 5, 6, 10}
print(s1.intersection(s2))  # Intersection: {3, 4, 5}
print(s1.difference(s2))    # Difference: {1, 10}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Frozen Set (frozenset)
# MAGIC A `frozenset` is an **immutable** version of a set.
# MAGIC - It **cannot** be modified after creation.
# MAGIC - Supports set operations but does **not** allow adding/removing elements.

# COMMAND ----------

# Creating a frozenset
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})

# Attempting to modify will raise an error
# fs.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

# Supports operations like union and intersection
fs2 = frozenset([3, 4, 5, 6])
print(fs.union(fs2))  # Output: frozenset({1, 2, 3, 4, 5, 6})
print(fs.intersection(fs2))  # Output: frozenset({3, 4})

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dictionary (dict)
# MAGIC A `dict` is a collection of key-value pairs.
# MAGIC - **Keys**: Must be unique and immutable (strings, numbers, tuples).
# MAGIC - **Values**: Can be of any data type.
# MAGIC - **Mutable**: Can add, update, or delete items.

# COMMAND ----------

# Creating dictionaries
d = {"name": "Shekhar", "age": 30, "city": "Patna"}
print(d)  # Output: {'name': 'Shekhar', 'age': 30, 'city': 'Patna'}

# Accessing values
print(d["name"])  # Output: Shekhar

# Adding & updating values
d["age"] = 31  # Update
print(d)  # Output: {'name': 'Shekhar', 'age': 31, 'city': 'Patna'}

d["country"] = "India"  # Add new key-value
print(d)  # Output: {'name': 'Shekhar', 'age': 31, 'city': 'Patna', 'country': 'India'}

# Removing key-value pairs
d.pop("city")
print(d)  # Output: {'name': 'Shekhar', 'age': 31, 'country': 'India'}

# Iterating over dictionary
for key, value in d.items():
    print(f"{key}: {value}")
# Output:
# name: Shekhar
# age: 31
# country: India
