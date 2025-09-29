# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
natural_numbers = [1,2,3,4,5,6,7,8,9,10]
product = 1
for i in range(1, 11):
    product *= i
print(f"Product of first 10 natural numbers: {product}")


# Your code here

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")

# Your code here
remainder = 156 % 7
print(f"Remainder :{remainder}")

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here
square = 25 ** 2
print(f"square:{square}")

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here
cube= pow(125, 1/3) 
print(f"Cube root :{cube}")

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
number = 12345
remainder = 0
sum_of_digits = 0
while number > 0 :
    remainder = number % 10
    sum_of_digits += remainder
    number /= 10   
print(f"Sum of digits: {sum_of_digits}")

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
n = 97
for i in range(2,n):
    if n % i == 0:
     print("97 is not a prime number.")
     break
else:
    print("97 is a prime number.")


# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
factorial = 1
for i in range(1, 9):
    factorial *= i 
print(f"Factorial of 8: {factorial}")   

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
numbers = [15, 23, 31, 42, 56]
average = sum(numbers) / len(numbers)       
print(f"Average: {average}")


# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here
import math
math.gcd(48, 36)  

print("-" * 50)


# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
# Your code here 
sum_of_odds = 0
for i in range(1, 40, 2):
    sum_of_odds += i    
print(f"Sum of first 20 odd numbers: {sum_of_odds}")