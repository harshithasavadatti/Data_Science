# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")
# Your code here
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
sum1 = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum1 += i
print(sum1)


# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
# Your code here
list1= [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print(set(list1))
# or
list1= [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
list2=[]
for x in list1:
    if x not in list2:
        list2.append(x)
print(f"list without duplicates : {list2}")
# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
# Your code here
list1= [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted list in descending order: {list1}")
# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
# Your code here

list1 = [15, 23, 31, 42, 56, 78, 91]
average = sum(list1) / len(list1)
print (average)
# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here
fib = [0, 1]
for i in range(2, 15):
    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)    
print(fib)
# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here
list1 = [45, 67, 23, 89, 12, 34, 78]
list1.sort(reverse=True)
second_largest = list1[1]
print(f"Second largest number: {second_largest}")
# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.reverse()
print(f"Reversed list: {list1}")
# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
# Your code here
list1 = [1, 5, 2, 5, 3, 5, 4, 5, 6]
count_five = list1.count(5)
print(f"Number of times 5 appears: {count_five}")

# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
# Your code here
prime = []
for i in range(2, 51):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print(f"Prime numbers between 1 and 50: {prime}")   
# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = []
for sublist in list1:
    for item in sublist:
        flatten.append(item)
print(f"Flattened list: {flatten}")
# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
# Your code here
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print(f"Common elements: {common_elements}")

# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
# Your code here
list1= [[1, 2], [3, 4], [5, 6]]
print(f"List of lists: {list1}")

# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in list1:
    sum_sub= sum(sublist)
    print(f"Sum of {sublist} is {sum_sub}") 

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)
for row in transposed:
    print(row)

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here
list1 = [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
for sublist in list1:
    max_value = max(sublist)
    print(f"Maximum value in {sublist} is {max_value}")     

# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
list3D = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(f"{list3D}")

# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
list1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
flatten =[]
for sublist1 in list1:
    for sublist2 in sublist1:
        for sublist3 in sublist2:
          flatten.append(sublist3)
sum1= sum(flatten)
print(f"Sum of 3D list : {sum1}")

# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_list =[]
for i in list1:
    for j in i:
        if j % 2 == 0:
           even_list.append(j)
print(f"Even list: {even_list}")

# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here
list1 = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"List of Mixed data types: {list1}")


# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here
list1 = ["apple", "banana", "cherry", "date"]
for items in list1:
    length = len(items)
    print(f"Length of '{items}' is {length}")   

# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
t = ((1, 'a'), (2, 'b'), (3, 'c'))
list1 = list(t)
print(f"List of tuples: {list1}")

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
list1 = [(1, 'a'), (2, 'b'), (3, 'c')]
list2=[]
for items in list1:
    list2.append(items[0])
print(f"First elements from each tuple: {list2}")

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here
dict1= {'name': 'Alice', 'age': 25}
dict2 ={'name': 'Bob', 'age': 30}
list1 = [dict1, dict2]
print(f"List of dictionaries: {list1}")
# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here
dict1= {'name': 'Alice', 'age': 25}
dict2 ={'name': 'Bob', 'age': 30}
list1 = [dict1, dict2]
names=[]
for name in list1:
    names.append(name['name'])
print ("names from the list of dictionaries :",names)
# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here
list1 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
oldest_person = max(list1, key=lambda person: person['age'])

print(f"Person with maximum age: {oldest_person}")


# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here
list1 = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print(f"4D list: {list1}")

# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here
list1 = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
flatten = []    
for sublist1 in list1:
    for sublist2 in sublist1:
        for sublist3 in sublist2:
            for item in sublist3:
                flatten.append(item)
max_value = max(flatten)
print(f"Maximum value in 4D list: {max_value}")

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here
list1 = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(f"List of sets: {list1}")

# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here
list1 = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
union_set = set()
for s in list1:
    union_set.update(s)
print(f"Union of all sets: {union_set}")

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here
complex_numbers = [1+2j, 3+4j, 5+6j]
print(f"List of complex numbers: {complex_numbers}")

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here
complex_numbers = [1+2j, 3+4j, 5+6j]
for num in complex_numbers:
    magnitude = abs(num)
    print(f"Magnitude of {num} is {magnitude}")
# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
# Your code here
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(f"Nested list: {nested_list}")

# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
# Your code here
nested_list = [1, [2, 3], [4, [5, 6]], 7]
def count_depth(lst):
    if isinstance(lst, list):
        return 1 + max(count_depth(item) for item in lst)
    else:
        return 0    
depth = count_depth(nested_list)
print(f"Depth of nesting: {depth}")

# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
# Your code here
functions = [len, str, int, float]
print(f"List of functions: {functions}")


# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
# Your code here
functions = [len, str, int, float]
string_value = "123"
for func in functions:
    result = func(string_value)
    print(f"Result of applying {func.__name__} to '{string_value}': {result}")

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
# Your code here
lambda_functions = [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print(f"List of lambda functions: {lambda_functions}")

# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
# Your code here
lambda_functions = [lambda x: x*2, lambda x: x**2, lambda x: x+1]
value = 5
for func in lambda_functions:
    result = func(value)
    print(f"Result of applying lambda function to {value}: {result}")


# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
# Your code here
list1 = [list, dict, set, tuple]
print(f"List of classes: {list1}")

# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
# Your code here
list1 = [list, dict, set, tuple]
for classes in list1:
    result= classes()
    print(result)

# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
# Your code here
none_list = [None, None, None, None]
print(f"List of None values: {none_list}")

# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
# Your code here
none_list = [None, None, None, None]
for values in list1:
    values= 0
    list2.append(values)
print(list2)

# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
# Your code here
bool_list = [True, False, True, False]
print(f"List of boolean values: {bool_list}")


# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
# Your code here
bool_list = [True, False, True, False]
count_true = bool_list.count(True)
print(f"Number of True values: {count_true}")

# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
# Your code here
list1 = [range(3), range(5), range(2)]
print(f"List of ranges: {list1}")


# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
# Your code here
list1 = [range(3), range(5), range(2)]
list2 = []
for r in list1:
    list2.append(list(r))
print(f"Converted ranges to lists: {list2}")


# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
# Your code here
list1 = [(x for x in range(3)), (x for x in range(5))]
print(f"List of generators: {list1}")

# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here
list1 = [(x for x in range(3)), (x for x in range(5))]
list2 = []
for gen in list1:
    list2.append(list(gen))
print(f"Converted generators to lists: {list2}")


# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
# Your code here

list1 = [iter([1, 2, 3]), iter([4, 5, 6])]
print(f"List of iterators: {list1}")

# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here 
list1 = [iter([1, 2, 3]), iter([4, 5, 6])]
list2 = []
for it in list1:
    list2.append(list(it))
print(f"Extracted elements from iterators: {list2}")

