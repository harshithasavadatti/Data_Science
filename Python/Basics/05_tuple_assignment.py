# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
# Your code here
numbers = tuple(range(1, 11))
print(f"Tuple of first 10 natural numbers: {numbers}")   
print("-" * 50)

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
# Your code here
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
length = len(numbers)
print(f"Length of the tuple: {length}")
print("-" * 50)

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
# Your code here
tuple1 = ('a', 'b', 'c', 'd', 'e')
element = tuple1[2] 
print(f"3rd element in the tuple: {element}")
print("-" * 50)

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
# Your code here
tuple1= (23, 45, 12, 67, 34, 89, 56)
max_value = max(tuple1)
print(f"Maximum value in the tuple: {max_value}")
print("-" * 50)

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
# Your code here
tuple1 = (1, 5, 2, 5, 3, 5, 4, 5, 6)
count = tuple1.count(5)
print(f"Number of times 5 appears: {count}")
print("-" * 50)

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
# Your code here
mixed_tuple = (42, 3.14, "Hello", True)
print(f"Mixed data types tuple: {mixed_tuple}")
print("-" * 50)

# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
# Your code here
tuple1 = ('java', 'python', 'c++', 'javascript')
i = tuple1.index('python')
print(f"Index of 'python': {i}")
print("-" * 50)

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
# Your code here
tuple1 = (10, 20, 30, 40, 50)
exists = 25 in tuple1
print(f"Does 25 exist in the tuple? {exists}")
print("-" * 50)

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
# Your code here
even_numbers = tuple(range(0, 10, 2))
print(f"Tuple of first 5 even numbers: {even_numbers}")
print("-" * 50)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
# Your code here 
tuple1 = (15, 23, 31, 42, 56, 78)
average = sum(tuple1) / len(tuple1)
print(f"Average of the numbers in the tuple: {average}")
print("-" * 50)