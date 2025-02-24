# Databricks notebook source
# MAGIC %md
# MAGIC # Binary Types in Python
# MAGIC Python provides several data types to handle binary data, including `bytes`, `bytearray`, and `memoryview`. 
# MAGIC These types are commonly used for handling raw binary data, working with files in binary mode, or optimizing memory usage.
# MAGIC
# MAGIC - **bytes**: Immutable sequence of bytes.
# MAGIC - **bytearray**: Mutable sequence of bytes.
# MAGIC - **memoryview**: Memory view object for accessing large binary data without copying it.

# COMMAND ----------

# Bytes: Immutable sequence of bytes
bytes_data = b"hello"
print("Bytes:", bytes_data)
print("Type of bytes_data:", type(bytes_data))

# COMMAND ----------

# Bytearray: Mutable sequence of bytes
bytearray_data = bytearray(b"hello")
print("Bytearray before modification:", bytearray_data)
bytearray_data[0] = ord('H')  # Modify the first byte
print("Bytearray after modification:", bytearray_data)

# COMMAND ----------

# Memoryview: Memory view object for accessing large data
memoryview_data = memoryview(bytearray_data)
print("Memoryview:", memoryview_data)
print("Memoryview first byte:", memoryview_data[0])  # Accessing the first byte
memoryview_data[0] = ord('h')  # Modify memory view data
print("Modified bytearray via memoryview:", bytearray_data)

# COMMAND ----------

# Demonstrating immutability of bytes (creates a new object)
new_bytes = bytes_data + b" world"
print("Original bytes_data:", bytes_data)
print("New bytes after concatenation:", new_bytes)

# COMMAND ----------

# Demonstrating mutability of bytearray (modification allowed)
bytearray_data.append(ord('!'))
print("Modified bytearray after append:", bytearray_data)

# COMMAND ----------

# Memoryview performance (no copying data)
import time
large_data = bytearray(10**6)  # 1 million bytes
mv = memoryview(large_data)

start_time = time.time()
# Accessing data using memoryview (efficient)
first_byte = mv[0]
end_time = time.time()
print(f"Memoryview access time: {end_time - start_time} seconds")

# COMMAND ----------

# **Features of Binary Types**

# 1. **Mutability**: 
#   - `bytes` are immutable. You cannot change the content of a `bytes` object.
#   - `bytearray` is mutable. You can modify its content directly.
#   - `memoryview` allows you to modify the underlying object if it’s mutable, like `bytearray`.

print(f"Is bytes_data mutable?: {'No'}") 
print(f"Is bytearray_data mutable?: {'Yes'}") 
print(f"Is memoryview_data mutable?: {'Yes' if mv[0] != 104 else 'No'}") 

# COMMAND ----------

# 2. **Indexing**: All binary types support indexing.
print("Indexing in bytes:", bytes_data[0])  # Accessing the first byte
print("Indexing in bytearray:", bytearray_data[0])  # Accessing the first byte
print("Indexing in memoryview:", memoryview_data[0])  # Accessing the first byte

# COMMAND ----------

# 3. **Slicing**: All binary types support slicing.
print("Slicing bytes:", bytes_data[:3])  # First three bytes
print("Slicing bytearray:", bytearray_data[:3])  # First three bytes
print("Slicing memoryview:", memoryview_data[:3])  # First three bytes

# COMMAND ----------

# 4. **Addition**: 
#   - `bytes` creates a new object when concatenated.
#   - `bytearray` allows direct modification like `append()`, `extend()`, or slicing.
#   - `memoryview` doesn't support addition directly but can be used to modify the underlying object.

# Addition on bytes (creates new object)
new_bytes = bytes_data + b" world"
print("Bytes after addition:", new_bytes)

# Addition on bytearray (modifies the object directly)
bytearray_data.extend(b" world")
print("Bytearray after addition:", bytearray_data)

# COMMAND ----------

# 5. **Deletion**:
#   - `bytes` does not support deletion or modification.
#   - `bytearray` supports deletion via `del`, `remove()`, or `pop()`.
#   - `memoryview` does not support deletion directly.

# Bytearray deletion example
del bytearray_data[5]  # Delete the character at index 5
print("Bytearray after deletion:", bytearray_data)

# COMMAND ----------

# 6. **Performance**: 
# - `bytes` and `tuple` (immutable types) are faster when used for simple operations.
# - `bytearray` (mutable) is slower due to overhead of supporting modification.
# - `memoryview` is the fastest for large datasets as it avoids copying data.

# Timing memoryview and bytearray access speed:
start_time = time.time()
for i in range(10**6):  # Iterate over 1 million bytes
    _ = bytearray_data[i]
end_time = time.time()
bytearray_time = end_time - start_time
print(f"Bytearray access time: {bytearray_time} seconds")

start_time = time.time()
for i in range(10**6):  # Iterate over 1 million bytes
    _ = mv[i]
end_time = time.time()
memoryview_time = end_time - start_time
print(f"Memoryview access time: {memoryview_time} seconds")

# COMMAND ----------

# Conclusion:
# - **bytes**: Immutable, used when data should not be changed.
# - **bytearray**: Mutable, used when data needs modification.
# - **memoryview**: Efficient for large data sets, avoids copying data.