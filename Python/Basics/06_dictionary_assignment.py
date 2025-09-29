# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
# Your code here
students = {'Alice': 20, 'Bob': 22, 'Charlie': 19, 'Diana': 21}
print(f"Student dictionary: {students}")

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
# Your code here
sample_dict = {'a': 1, 'b': 2, 'c': 3}
sample_dict['d'] = 4
print(f"Updated dictionary: {sample_dict}")

# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
# Your code here
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
keys = sample_dict.keys()
print(f"Keys in dictionary: {keys}")

# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
# Your code here
sample_dict = {'python': 3, 'java': 2, 'c++': 1}
values = sample_dict.values()
print(f"Values in dictionary: {values}")

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
# Your code here
sample_dict = {'name': 'Alice', 'age': 30, 'city': 'London'}
key_exists = 'age' in sample_dict
print(f"Does 'age' key exist? {key_exists}")

# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
# Your code here
sample_dict = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
if 'temp' in sample_dict:
    del sample_dict['temp']
print(f"Dictionary after removing 'temp': {sample_dict}")

# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
# Your code here
sample_dict = {'math': 85, 'science': 92, 'english': 78}
total_sum = sum(sample_dict.values())
print(f"Sum of all values: {total_sum}")

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
# Your code here
squares = {}
for i in range(1, 6):
    squares[i] = i ** 2
print(f"Squares dictionary: {squares}")

# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
# Your code here
sample_string = "hello"
char_count = {}
for char in sample_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"Character frequency: {char_count}")

# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
# Your code here
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
# Your code here
nested_dict = {'person': {'name': 'Alice', 'age': 25}}
print(f"Nested dictionary: {nested_dict}")

# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
# Your code here
nested_dict = {'person': {'name': 'Alice', 'age': 25}}
name_value = nested_dict['person']['name']
print(f"Accessed nested name: {name_value}")

# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
# Your code here
fruits_dict = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print(f"Dictionary with list values: {fruits_dict}")

# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
# Your code here
fruits_dict = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
fruits_dict['fruits'].append('orange')
print(f"Updated fruits list: {fruits_dict['fruits']}")

# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
# Your code here
tuple_dict = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(f"Dictionary with tuple values: {tuple_dict}")

# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
# Your code here
tuple_dict = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
first_coordinate = tuple_dict['coordinates'][0]
print(f"First coordinate: {first_coordinate}")

# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
# Your code here
set_dict = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print(f"Dictionary with set values: {set_dict}")


# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
# Your code here
set_dict = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
set_dict['vowels'].add('o')
print(f"Updated vowels set: {set_dict['vowels']}")

# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
# Your code here
nested_dict = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(f"3-level nested dictionary: {nested_dict}")

# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
# Your code here
nested_dict = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
employee_name = nested_dict['company']['department']['employee']['name']
print(f"Accessed employee name: {employee_name}")

# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
# Your code here
mixed_dict = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print(f"Mixed data types dictionary: {mixed_dict}")

# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
# Your code here
mixed_dict = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
for key, value in mixed_dict.items():
    print(f"Key: {key}, Value: {value}, Type: {type(value)}")


# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
# Your code here
function_dict = {'len': len, 'str': str, 'int': int}
print(f"Dictionary with function values: {function_dict}")

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
# Your code here
function_dict = {'len': len, 'str': str, 'int': int}
input_value = "123"
print(function_dict['len'](input_value))
print(function_dict['str'](input_value))
print(function_dict['int'](input_value))

# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
# Your code here
lambda_dict = {'double': lambda x: x * 2, 'square': lambda x: x ** 2}
print(f"Dictionary with lambda functions: {lambda_dict}")

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
# Your code here
lambda_dict = {'double': lambda x: x * 2, 'square': lambda x: x ** 2}
print(lambda_dict['double'](5))
print(lambda_dict['square'](5))

# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
# Your code here
class_dict = {'list': list, 'dict': dict, 'set': set}
print(f"Dictionary with class values: {class_dict}")

# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")
# Your code here
class_dict = {'list': list, 'dict': dict, 'set': set}
list_instance = class_dict['list']([1, 2, 3])
dict_instance = class_dict['dict']({'a': 1, 'b': 2})
set_instance = class_dict['set']({1, 2, 3})
print(f"List instance: {list_instance}")
print(f"Dict instance: {dict_instance}")
print(f"Set instance: {set_instance}")

# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
# Your code here
none_dict = {'a': None, 'b': None, 'c': None}
print(f"Dictionary with None values: {none_dict}")

# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
# Your code here
none_dict = {'a': None, 'b': None, 'c': None}
for key in none_dict:
    if none_dict[key] is None:
        none_dict[key] = 0
print(f"Dictionary after replacing None with 0: {none_dict}")

# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
# Your code here
bool_dict = {'is_active': True, 'is_admin': False}
print(f"Dictionary with boolean values: {bool_dict}")

# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
# Your code here
bool_dict = {'is_active': True, 'is_admin': False}
count=0
for value in bool_dict.values():
    if value is True:
        count= count+1
print(count)

# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
# Your code here
complex_dict = {'z1': 3 + 4j, 'z2': 1 + 2j}
print(f"Dictionary with complex numbers: {complex_dict}")

# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
# Your code here
complex_dict = {'z1': 3 + 4j, 'z2': 1 + 2j}
print(abs(complex_dict["z1"]))
print(abs(complex_dict["z2"]))


# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
# Your code here
nested_dict = {
    'level1': {
        'level2': {
            'level3': {
                'level4': {
                    'key': 'value'
                }
            }
        }
    }
}
print(f"4-level nested dictionary: {nested_dict}")

# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
# Your code here
nested_dict = {
    'level1': {
        'level2': {
            'level3': {
                'level4': {
                    'key': 'value'
                }
            }
        }
    }
}
deepest_value = nested_dict['level1']['level2']['level3']['level4']['key']
print(f"Accessed deepest value: {deepest_value}")


# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
# Your code here
dict1 = {'r1': range(3), 'r2': range(5)}
print(f"Dictionary with range values: {dict1}")

# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
# Your code here
dict1={ "r1": range(3), "r2":range(5)}
for keys in dict1:
    dict1[keys]= list(dict1[keys])
print(f"list dictionary is : {dict1}")

# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
# Your code here
dict1 = {'gen1': (x for x in range(3)), 'gen2': (x for x in range(5))}
print(f"Dictionary with generator values: {dict1}")

# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
# Your code here
dict1 = {'gen1': (x for x in range(3)), 'gen2': (x for x in range(5))}
for key in dict1:
    dict1[key] = list(dict1[key])
print(f"Converted generators to lists: {dict1}")

# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
# Your code here
dict1 = {'iter1': iter([1, 2, 3]), 'iter2': iter([4, 5, 6])}
print(f"Dictionary with iterator values: {dict1}")

# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
# Your code here
dict1 = {'iter1': iter([1, 2, 3]), 'iter2': iter([4, 5, 6])}
extracted_elements = {}
for key, it in dict1.items():
    extracted_elements[key] = list(it)
print(f"Extracted elements from iterators: {extracted_elements}")

# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
# Your code here
nested_list_dict = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print(f"Dictionary with nested lists: {nested_list_dict}")

# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
# Your code here

# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
# Your code here
nested_dict = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(f"Nested dictionary with configuration: {nested_dict}")   

# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
# Your code here
nested_dict = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
db_port = nested_dict['config']['db']['port']
print(f"Accessed database port: {db_port}")

# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
# Your code here
nested_tuple_dict = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print(f"Dictionary with nested tuples: {nested_tuple_dict}")


# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
# Your code here
nested_tuple_dict = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
first_point = nested_tuple_dict['points'][0]    
print(f"First point coordinates: {first_point}")

# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
# Your code here
nested_set_dict = {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print(f"Dictionary with nested sets: {nested_set_dict}")

# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
# Your code here 
nested_set_dict = {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
all_sets = set()
for nested_set in nested_set_dict.values():
    for s in nested_set:
        all_sets.update(s)
print(f"Union of all nested sets: {all_sets}")  