# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
# Your code here
string = "Python Programming"
reverse = string[::-1]
print(f"reversed string : {reverse}")
print("-" * 50)
# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
# Your code here
string= "racecar"
reverse = string[::-1]
if string == reverse:
    print(f"{string} is a palindrome")    
else:
    print(f"{string} is not a palindrome")    

print("-" * 50)
   
# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
# Your code here
string = "Python is a great programming language"
string_list = string.split()
word_count = len(string_list)
print(f"Number of words: {word_count}")

print("-" * 50)

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
# Your code here
string = "hello world"  
title_case = string.title()
print(f"Title case: {title_case}")  

print("-" * 50)

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
# Your code here
string = "Data Science"
string_length = len(string)
print(f"Length of string: {string_length}")

print("alternative using list")
string2= list(string)
print(f"Length : {len(string2)}")
print("-" * 50)

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
# Your code here
string = "Machine Learning"
new_string =string.replace(" ", "_")
print(f"String with underscores: {new_string}") 

print("-" * 50)
# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
# Your code here
string = "Python Programming Language"
print("python" in string)

print("-" * 50)

# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
# Your code here
string = "Artificial Intelligence"
print(f"First 5 characters: {string[:5]}")

print("-" * 50)

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
# Your code here
string = "UPPERCASE"
print(f"Lowercase: {string.lower()}")

print("-" * 50)

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
# Your code here
string = "Computer Science"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print(f"After removing Vowels: {result}" )   
# https://prepinsta.com/python-program/to-remove-the-vowels-from-a-string/  reference
# using translate method
string = "Computer Science"
table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
string2 = string.translate(table)
print(f"String without vowels: {string2}")

print("-" * 50)

# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
# Your code here
from collections import Counter
s = "mississippi"
frequency = Counter(s)
max_char = max(frequency, key=frequency.get)
print(max_char)

# another method 
most_freq = max(set(s),key = s.count)
print("Frequent character:", most_freq)
print("-" * 50)

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
# Your code here
s1 = "listen"  
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("its an anagram")
else:
    print("Not an anagram")

print("-" * 50)

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
# Your code here
string = "python programming language"
capitalized_string = string.title() 
print(f"Capitalized string: {capitalized_string}")

print("-" * 50)


# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
# Your code here
string = "Hello World"
string = string.lower()
consonants = "bcdfghjklmnpqrstvwxyz"
count = 0
for x in string:
    if x in consonants:
        count += 1
print("Total Number of Consonants in this String = ", count)

print("-" * 50)

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
# Your code here
string = "Python is a programming language"
words = string.split()
result = max(words, key=len)
print(f"Longest word in the string : {result}")
# print("2nd method \n")
# words = string.split()
# res = ""
# for word in words:
#     if len(word) > len(res):
#         res = word
# print(res)
print("-" * 50)

# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
# Your code here
string = "Hello, World! How are you?"
punctuations = "!?,"
for x in string.lower():
    for x in punctuations:
        string = string.replace(x,"")
print(f"string without punctuations :{string }")

print("-" * 50)


# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
# Your code here
string = "Python is a Programming language"
y ="Python"
x = string.startswith(y)
print(f"Does the sentence start with {y}:{x}")

print("-" * 50)

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
# Your code here
string = "Hello World"
index = string.find('o')    
print("Occurance of 'o' is at index:", index)
print("-" * 50)

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
# Your code here
string = "apple,banana,orange"
split_string = string.split(',')
print(f"Split string: {split_string}")
print("-" * 50)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
# Your code here

list_of_strings = ['Python', 'is', 'awesome']
joined_string = ' '.join(list_of_strings)  
print(f"Joined string: {joined_string}") 
print("-" * 50)

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here
s ="12345"
x = s.isdigit()
print(f"string contains only digits :{x}")


print("-" * 50)

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here
s ="HelloWorld"
x = s.isalpha()
print(f"string contains only alphabets :{x}")

print("-" * 50)

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here
string = "hello world"
result = ""
count = 0  # only for letters
for char in string:
    if char == " ":
        result += " "
    else:
        if count % 2 == 0:
            result += char.lower()
        else:
            result += char.upper()
        count += 1
print(f"Alternating case string: {result}")

print("-" * 50)

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here
string = "banana"
for i in range(len(string)):
    if string[i] == 'a':
        print(f"'a' found at index: {i}")   
print("-" * 50)

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here
string = "  Hello World  "
x = string.strip()
print(f"String without leading and trailing whitespace :{x}")
print("-" * 50)

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here
s= "programming"
x= s.endswith("ing")
print(x)

print("-" * 50)
# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here
string = "Hello World"
new = string.replace('o', '0', 1) 
print("new")
print("-" * 50)


# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here

string = "Python is a programming language"
words = string.split()
result = min(words, key=len)
print(f"shortest word in the string : {result}")
print("-" * 50)

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here
string = "Python programming is powerful"
string = string.lower()
wordcount= 0
for word in string.split():
    if word.startswith("p"):
      wordcount+=1
print(f"Words that start with 'p':{wordcount}")
print("-" * 50)

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
string ="Hello World Python"
reverse =string[::-1]
#reversed_string = ' '.join(string.split()[::-1])
print(reverse)

print("-" * 50)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here
email = "user@example.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# import re

# email = "user@example.com"
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# if re.match(pattern, email):
#     print("Valid email format")
# else:
#     print("Invalid email format")

print("-" * 50)

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here
string = "https://www.example.com/path"
domain = string.split("//")[1].split("/")[0]
print(f"Domain: {domain}")
print("-" * 50)

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here
text = """This is line one.
This is line two.   
This is line three."""
line_count = len(text.split("\n"))
print(f"Number of lines: {line_count}") 
#can be done using splitlines() method and count+1 
print("-" * 50)

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here
str1 = "hello"
str2 = "world" 
common = ""  
for char in str1:
    if char in str2 and char not in common:
        common += char
print(f"Common characters: {common}")

#using set and intersection
set1 = set(str1)    
set2 = set(str2)
common_chars = set1.intersection(set2)
print(f"Common characters using set: {common_chars}")

print("-" * 50)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here
number = "+1-555-123-4567"

if number.startswith("+") and "-" in number:
    parts = number.split("-")
    if (
        len(parts) == 4 and
        parts[0][1:].isdigit() and
        all(part.isdigit() for part in parts[1:])
    ):
        print("Valid phone number")
    else:
        print("Invalid phone number")
else:
    print("Invalid phone number")
print("-" * 50)

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
text = "abc123def456ghi789"
number = ""
for char in text:
    if char.isdigit():
        number += char
print(f"All digits together: {number}")

# Your code here
print("-" * 50)

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here
snake = "snake_case"
parts = snake.split("_")
camel = parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(f"camelCase: {camel}")

print("-" * 50)

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here
string = "A man a plan a canal Panama"
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("It's a palindrome")  
else:
    print("It's not a palindrome")
print("-" * 50)

# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here
text = "the quick brown fox jumps over the lazy dog"

words = text.split()
most_common = ""
max_count = 0

for word in words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        most_common = word

print(f"Most common word: {most_common} \nOccurence: {max_count} times")

print("-" * 50)

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here
string = "National Aeronautics and Space Administration"
string = string.split()
acronym = ""
for word in string:
    if word not in ["and"]:
     acronym += word[0].upper()
print(f"Acronym: {acronym}")

print("-" * 50)


# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here
s = "((()))"
count = 0

for ch in s:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1
    if count < 0:
        break  # More ')' than '(' at this point

if count == 0:
    print("Balanced")
else:
    print("Not Balanced")

print("-" * 50)

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here
text = "hello world"
morse_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.', 'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....', 'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',   'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',  's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',  'x': '-..-',  'y': '-.--',
    'z': '--..',  ' ': '/'
}

morse_code = ""

for char in text.lower():
    morse_code += morse_dict.get(char, '') + ' '

print(f"Morse Code: {morse_code.strip()}")

print("-" * 50)

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here
s1 = "programming"
s2 = "grammar"
longest = ""

for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        substring = s1[i:j]
        if substring in s2 and len(substring) > len(longest):
            longest = substring

print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
print(f"Longest common substring: '{longest}'")
print("-" * 50)

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here
# string = "https://www.google.com"
# if string.startswith("http://") or string.startswith("https://"):
    
print("-" * 50)

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here
text = "Python programming is amazing and powerful"
words = text.split()
for word in words:
    if len(word) > 5:
        print(word)

print("-" * 50)

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
text = "hello world"
text = text.split()
pig_latin_final=[]
for word in text:
  if word[0] in "aeiou":
      pig_latin = word +"way"
      pig_latin_final.append(pig_latin)
  else:
      pig_latin = word[1:]+word[0]+"ay"
      pig_latin_final.append(pig_latin)
print(' '.join(pig_latin_final))

# Your code here
print("-" * 50)

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here
ip = "192.168.1.1"
parts = ip.split('.')

if len(parts) == 4:
    for part in parts:
        if not (part.isdigit() and 0 <= int(part) <= 255 and part == str(int(part))):
            print("Not a valid IPv4 address")
            break
    else:
        print("Valid IPv4 address")  # Runs only if loop didn't break
else:
    print("Not a valid IPv4 address")


# if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
#     print("Valid IPv4 address") 
# else:
#     print("Not valid")
print("-" * 50)

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here
string = "abc"
s = "abc"
substrings = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])
print(substrings)
print("-" * 50)

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here
print("-" * 50)

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 
print("-" * 50)
