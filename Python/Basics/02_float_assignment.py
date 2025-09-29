# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here
numbers = [3.14, 2.718, 1.618, 0.577]
average = sum(numbers) / len(numbers)       
print(f"Average: {average}")
print("-" * 50)

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here
f= 98.6
c = (f - 32) * 5/9
print(f"Fahrenheit: {f}")
print("-" * 50)

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here
p = 1000
r = 5.5
t = 3
amount = p *(pow((1 + r / 100), t))
c_i= amount - p
print(f"compound interest: {c_i}")
print("-" * 50)

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here
a = 3.5
b = 4.2 
c = math.sqrt(pow(a, 2) + pow(b, 2 ))
print(f"Hypotenuse: {c}")
print("-" * 50)


# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here
r = 7.8
pi = math.pi
v = (4/3) *pi  * pow(r, 3)
print("-" * 50)


# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here
number = 3.14159
rounded_number = round(number, 3)
print(f"Rounded number: {rounded_number}")

print("-" * 50)

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here
percentage = (45 / 67) * 100
print(f"Percentage: {percentage}%")

print("-" * 50)

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here
sqrt_value = math.sqrt(23.456)
print(f"Square root: {sqrt_value}")

print("-" * 50)


# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here
Principal=2500
Rate=6.5
Time=2.5
simple_interest = (Principal * Rate * Time)/100
print(f"Simple Interest: {simple_interest}")

print("-" * 50)


# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 
radians = math.radians(45.7)
print(f"Radians: {radians}")

radians = 45.7 * (math.pi / 180)
print(f"Radians: {radians}")