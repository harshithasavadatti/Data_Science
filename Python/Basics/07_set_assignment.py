# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
# Your code here
set_natural_numbers = set(range(1, 11))
print(f"Set of first 10 natural numbers: {set_natural_numbers}")

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
# Your code here
set1 = {1, 2, 3, 4, 5}
set1.add(11)
print(f"Set after adding 11: {set1}")

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
# Your code here
set2 = {1, 2, 3, 4, 5, 6}
set2.discard(3)
print(f"Set after removing 3: {set2}")

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference_set = set1.difference(set2)
print(f"Difference: {difference_set}")

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
# Your code here
set1 = {1, 2, 3, 4, 6, 7, 8}
exists = 5 in set1
print(f"Does 5 exist in the set? {exists}")

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
# Your code here
set1 = {'a', 'b', 'c', 'd', 'e'}
length = len(set1)
print(f"Length of the set: {length}")

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
# Your code here
string = "hello world"
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_set = set()
for char in string:
    if char in vowels:
        vowel_set.add(char)
print(f"Set of vowels in 'hello world': {vowel_set}")
# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
# Your code here
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_set = set(list_with_duplicates)
print(f"Set after removing duplicates: {unique_set}")

# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
# Your code here 
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}
is_subset = set1.issubset(set2)
print(f"subset:{is_subset}")