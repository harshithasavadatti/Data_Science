# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
# Your code here
z = 5 + 3j
print(f"Complex number: {z}")
print("-" * 50)

# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
# Your code here
i = 7 - 2j
print (i.real)
print("-" * 50)

# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
# Your code here
i = 4 + 6j
print (i.imag)
print("-" * 50)

# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
# Your code here
z1 = 3 + 2j
z2 = 1 + 4j
result = z1 + z2
print(f"Sum of complex numbers: {result}")
print("-" * 50)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
# Your code here
z1 = 2 + 3j
z2 = 1 + 2j
result = z1 * z2
print(f"Product of complex numbers: {result}")
print("-" * 50)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
# Your code here
z = 6 + 8j
magnitude = abs(z)
print(f"Magnitude of complex number {z}: {magnitude}")
print("-" * 50)

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
# Your code here
z = 5 - 7j
conjugate = z.conjugate()
print(f"Conjugate of complex number {z}: {conjugate}")
print("-" * 50)

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
# Your code here
z1 = 10 + 5j
z2 = 3 + 2j
result = z1 - z2
print(f"Difference of complex numbers: {result}")
print("-" * 50)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
# Your code here
z1 = 8 + 6j
z2 = 2 + 1j
result = z1 / z2
print(f"Division of complex numbers: {result}")
print("-" * 50)

# Question 10: Find the phase angle of complex number 1 + 1j
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
# Your code here 
import cmath
z = 1 + 1j
phase_angle = cmath.phase(z)
print(f"Phase angle of complex number {z}: {phase_angle} radians")
print("-" * 50)