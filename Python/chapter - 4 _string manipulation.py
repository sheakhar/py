# Databricks notebook source
# 5. String Manipulation in Python
# This notebook covers various string manipulation techniques in Python, 
# including counting substrings, replacing strings, splitting, joining, and changing the case of strings. 
# Additionally, we will explore string validation methods and common operators.

# COMMAND ----------

# 1. Counting Substrings
# Example: Count Occurrences of a Substring

# Define the main string and the substring you want to count
main_string = "Python is great. Python is dynamic. Python is popular."
substring = "Python"

# Count the occurrences
count = main_string.count(substring)
print(f"The substring '{substring}' occurred {count} times in the main string.")

# COMMAND ----------

# Example: Count with Begin and End Index

# Count occurrences of 'Python' between index 10 and 50
count_in_range = main_string.count(substring, 10, 50)
print(f"The substring '{substring}' occurred {count_in_range} times in the range 10 to 50.")

# COMMAND ----------

# 2. Replacing Strings
# Example: Replace a Substring with Another

# Replace 'Python' with 'Databricks'
new_string = main_string.replace('Python', 'Databricks')
print(new_string)

# COMMAND ----------

# 3. Splitting Strings
# Example: Splitting by a Separator

# Split the string into a list
split_list = main_string.split('. ')
print(split_list)

# COMMAND ----------

# 4. Joining Strings
# Example: Joining a List into a String

# Define a list of words
words_list = ['durga', 'soft', 'solutions']

# Join the list into a single string with '-'
joined_string = '-'.join(words_list)
print(joined_string)

# COMMAND ----------

# 5. Changing Case of Strings
# Example: Change String Case

s = 'The Python Classes By Durga Sir'

print(s.upper())      # Convert to upper case
print(s.lower())      # Convert to lower case
print(s.swapcase())   # Swap case
print(s.title())      # Title case
print(s.capitalize()) # Capitalize

# COMMAND ----------

# 6. String Validation and Common Operations
# Example: Check Alphanumeric Characters

print(s.isalnum()) # Checks if all characters are alphanumeric

other_sample = "Python3"

print(other_sample.isalpha()) # Checks if all characters are alphabetic
print(other_sample.isdigit()) # Checks if all characters are digits
print(other_sample.islower()) # Checks if all characters are lowercase
print(other_sample.isupper()) # Checks if all characters are uppercase
print(other_sample.istitle()) # Checks if the string is title-cased
print(other_sample.isspace()) # Checks if the string contains only spaces

# COMMAND ----------

# 7. Additional String Operations
# Example: Miscellaneous Operations

print(len(s))       # Get the length of the string
print('Python' in s)  # Check if substring is in the string
print('Java' not in s) # Check if substring is not in the string

# Strip operations
trimmed_string = "  Hello World  ".strip()
print(trimmed_string)

# COMMAND ----------

# 8. Questions and Solutions: Advanced String Manipulation Techniques

# 8.1 Counting Substrings with a Condition
# Description: Write a function to count the occurrences of a substring with a specific condition.

def count_vowel_start_substrings(main_string, substring):
    vowels = "AEIOUaeiou"
    return sum(1 for i in range(len(main_string) - len(substring) + 1)
               if main_string[i:i + len(substring)] == substring and 
               (i == 0 or main_string[i-1] in vowels))

# Example usage:
main_string = "Example easy but exceptional example"
substring = "exam"
print(count_vowel_start_substrings(main_string, substring))

# COMMAND ----------

# 8.2 Custom Replacement Logic
# Description: Implement replacement for the first 'n' occurrences of a substring.

def replace_first_n(main_string, old, new, n):
    split_str = main_string.split(old)
    result = new.join(split_str[:n+1]) + old.join(split_str[n+1:])
    return result

# Example usage:
main_string = "Python is fun. Python is popular. Python is great."
print(replace_first_n(main_string, "Python", "Databricks", 2))

# COMMAND ----------

# 8.3 Splitting Strings with Multiple Delimiters
# Description: Use regular expressions to split a string with multiple delimiters.

import re

def split_multiple_delimiters(main_string):
    return re.split(r'[,.]', main_string)

# Example usage:
main_string = "Split, this. string, by. commas, and. periods."
print(split_multiple_delimiters(main_string))

# COMMAND ----------

# 8.4 Joining with Conditions
# Description: Join words longer than a specified length.

def join_long_words(words_list):
    return '-'.join(word for word in words_list if len(word) >= 5)

# Example usage:
words_list = ['durga', 'soft', 'solutions', 'is', 'great']
print(join_long_words(words_list))

# COMMAND ----------

# 8.5 Case Conversion Conditional
# Description: Convert case based on the starting character of each word.

def lower_case_consonant_start(s):
    words = s.split()
    result = [word.lower() if word[0].lower() not in "aeiou" else word for word in words]
    return ' '.join(result)

# Example usage:
s = "This Is An Example String"
print(lower_case_consonant_start(s))

# COMMAND ----------

# 8.6 Alphanumeric Split
# Description: Split a string and return a list of tuples indicating if each word is alphanumeric.

def split_and_check_alnum(s):
    words = s.split()
    return [(word, word.isalnum()) for word in words]

# Example usage:
s = "Python3 is a great 123 programming#language"
print(split_and_check_alnum(s))

# COMMAND ----------

# 8.7 Reversing Word Order
# Description: Reverse the order of words in a string.

def reverse_word_order(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

# Example usage:
sentence = "Welcome to the world of Python"
print(reverse_word_order(sentence))

# COMMAND ----------

# 8.8 Middle Third Extraction
# Description: Extract the middle third of a string.

def middle_third(s):
    length = len(s)
    if length < 3:
        return "String is too short"
    third = length // 3
    return s[third:2*third]

# Example usage:
s = "abcdefghijklmnop"
print(middle_third(s))

# COMMAND ----------

# 8.9 Regular Expression Email Validation
# Description: Validate if a string is a valid email address format.

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Example usage:
email = "example@domain.com"
print(is_valid_email(email))

# COMMAND ----------

# 8.10 Title Case Custom
# Description: Convert a sentence to title case, keeping certain words lowercase.

def custom_title_case(sentence, exceptions):
    words = sentence.split()
    title_cased = [word if word in exceptions else word.title() for word in words]
    return ' '.join(title_cased)

# Example usage:
sentence = "the quick brown fox jumps over the lazy dog"
exceptions = {"the", "over"}
print(custom_title_case(sentence, exceptions))

# COMMAND ----------

# 8.11 Whitespace Normalization
# Description: Normalize whitespace by converting multiple spaces to a single space.

def normalize_whitespace(s):
    return ' '.join(s.split())

# Example usage:
s = " This   is  an  example    string  "
print(normalize_whitespace(s))

# COMMAND ----------

# 8.12 Substring Check without Built-ins
# Description: Check if a substring exists within a string without using the 'in' operator.

def substring_exists(main_string, substring):
    sub_length = len(substring)
    for i in range(len(main_string) - sub_length + 1):
        if main_string[i:i + sub_length] == substring:
            return True
    return False

# Example usage:
main_string = "Python is great"
substring = "great"
print(substring_exists(main_string, substring))

# COMMAND ----------

# 8.13 Character Frequency Counter
# Description: Count the frequency of each character in a string.

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage:
s = "hello world"
print(char_frequency(s))

# COMMAND ----------

# 8.14 Custom Strip Function
# Description: Remove a specific character from the beginning and end of a string.

def custom_strip(s, char_to_remove):
    start, end = 0, len(s) - 1
    while start <= end and s[start] == char_to_remove:
        start += 1
    while end >= start and s[end] == char_to_remove:
        end -= 1
    return s[start:end+1]

# Example usage:
s = "###hello world###"
print(custom_strip(s, "#"))

# COMMAND ----------

# 8.15 Comparison Without Case Sensitivity
# Description: Compare two strings for equality, ignoring case differences.

def compare_strings_ignore_case(s1, s2):
    return s1.lower() == s2.lower()

# Example usage:
s1 = "Python"
s2 = "pYTHON"
print(compare_strings_ignore_case(s1, s2))