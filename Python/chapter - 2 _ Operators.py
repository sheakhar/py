# Databricks notebook source
# MAGIC %md
# MAGIC 1. Arithmetic Operators
# MAGIC Used for mathematical operations.
# MAGIC
# MAGIC Operator	Description	Example (a = 10, b = 3)	Result
# MAGIC +	Addition	a + b	13
# MAGIC -	Subtraction	a - b	7
# MAGIC *	Multiplication	a * b	30
# MAGIC /	Division (float)	a / b	3.3333
# MAGIC //	Floor Division	a // b	3
# MAGIC %	Modulus (remainder)	a % b	1
# MAGIC **	Exponentiation	a ** b	1000
# MAGIC 2. Comparison (Relational) Operators
# MAGIC Used for comparing values.
# MAGIC
# MAGIC Operator	Description	Example (a = 10, b = 3)	Result
# MAGIC ==	Equal to	a == b	False
# MAGIC !=	Not equal to	a != b	True
# MAGIC >	Greater than	a > b	True
# MAGIC <	Less than	a < b	False
# MAGIC >=	Greater than or equal to	a >= b	True
# MAGIC <=	Less than or equal to	a <= b	False
# MAGIC 3. Logical Operators
# MAGIC Used to combine conditional statements.
# MAGIC
# MAGIC Operator	Description	Example (x = True, y = False)	Result
# MAGIC and	Returns True if both conditions are true	x and y	False
# MAGIC or	Returns True if at least one condition is true	x or y	True
# MAGIC not	Reverses the condition	not x	False
# MAGIC 4. Bitwise Operators
# MAGIC Works at the bit level.
# MAGIC
# MAGIC Operator	Description	Example (a = 10 (1010), b = 3 (0011))	Result (Binary)
# MAGIC &	AND	a & b	2 (0010)
# MAGIC `	`	OR	`a
# MAGIC ^	XOR	a ^ b	9 (1001)
# MAGIC ~	NOT	~a	-11
# MAGIC <<	Left shift	a << 1	20 (10100)
# MAGIC >>	Right shift	a >> 1	5 (0101)
# MAGIC 5. Assignment Operators
# MAGIC Used to assign values to variables.
# MAGIC
# MAGIC Operator	Example	Equivalent To
# MAGIC =	a = 10	a = 10
# MAGIC +=	a += 2	a = a + 2
# MAGIC -=	a -= 2	a = a - 2
# MAGIC *=	a *= 2	a = a * 2
# MAGIC /=	a /= 2	a = a / 2
# MAGIC //=	a //= 2	a = a // 2
# MAGIC %=	a %= 2	a = a % 2
# MAGIC **=	a **= 2	a = a ** 2
# MAGIC &=	a &= 2	a = a & 2
# MAGIC `	=`	`a
# MAGIC ^=	a ^= 2	a = a ^ 2
# MAGIC <<=	a <<= 2	a = a << 2
# MAGIC >>=	a >>= 2	a = a >> 2
# MAGIC 6. Identity Operators
# MAGIC Used to compare memory locations of objects.
# MAGIC
# MAGIC Operator	Description	Example (a = [1, 2, 3], b = a, c = [1, 2, 3])	Result
# MAGIC is	Returns True if objects are the same	a is b	True
# MAGIC is not	Returns True if objects are different	a is not c	True
# MAGIC 7. Membership Operators
# MAGIC Used to check if a value exists in a sequence.
# MAGIC
# MAGIC Operator	Description	Example (x = [1, 2, 3])	Result
# MAGIC in	Returns True if value is in sequence	2 in x	True
# MAGIC not in	Returns True if value is not in sequence	4 not in x	True

# COMMAND ----------

# 1. Arithmetic Operators
# These operators perform mathematical operations like addition, subtraction, multiplication, etc.
a = 10
b = 3
print("Addition:", a + b)      # 13
print("Subtraction:", a - b)   # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.3333
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)       # 1
print("Exponentiation:", a ** b) # 1000

# COMMAND ----------

# 2. Comparison Operators
# These operators compare values and return True or False
a = 10
b = 3
print("Equal:", a == b)      # False
print("Not Equal:", a != b)  # True
print("Greater:", a > b)     # True
print("Less:", a < b)       # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)   # False

# COMMAND ----------

# 3. Logical Operators
# Used to combine conditional statements
x = True
y = False
print("AND:", x and y) # False
print("OR:", x or y)  # True
print("NOT:", not x)   # False

# COMMAND ----------

# 4. Bitwise Operators
# Bitwise operators perform operations on the binary representation of integers.
# The basic formulas used for bitwise operations are:
# Bitwise AND (&):  result = a & b (only 1 if both bits are 1)
# Bitwise OR (|):   result = a | b (1 if at least one bit is 1)
# Bitwise XOR (^):  result = a ^ b (1 if bits are different)
# Bitwise NOT (~):  result = ~a (inverts bits, equivalent to -(a+1))
# Left Shift (<<):  result = a << n (shifts bits left by n places, equivalent to a * 2^n)
# Right Shift (>>): result = a >> n (shifts bits right by n places, equivalent to a // 2^n)

a = 10  # 1010
b = 3   # 0011
print("Bitwise AND:", a & b) # 2  (0010)
print("Bitwise OR:", a | b)  # 11 (1011)
print("Bitwise XOR:", a ^ b) # 9  (1001)
print("Bitwise NOT:", ~a)    # -11 formula = -(a+1)
print("Left Shift:", a << 1) # 20 (10100)
print("Right Shift:", a >> 1) # 5 (0101)

# COMMAND ----------

# 5. Assignment Operators
# Used to assign values to variables
a = 5
a += 3  # a = a + 3
print("a after +=:", a) # 8
a *= 2  # a = a * 2
print("a after *=:", a) # 16
a //= 4  # a = a // 4
print("a after //=:", a) # 4

# COMMAND ----------

# 6. Identity Operators
# Check if two objects refer to the same memory location
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y) # True
print("x is z:", x is z) # False

# COMMAND ----------

a=3
b=3
a is b

# COMMAND ----------

# 7. Membership Operators
# Check if a value exists in a sequence
lst = [1, 2, 3, 4, 5]
print("3 in lst:", 3 in lst)     # True
print("6 not in lst:", 6 not in lst) # True