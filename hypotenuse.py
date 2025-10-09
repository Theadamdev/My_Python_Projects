#calculate the hypotenuse of a right triangle when given the two oher sides
import math
a = float(input("Enter the length of the first side of the triangle : "))
b = float(input("Enter the length of the second side of the triangle : "))
c = math.sqrt(a**2 + pow(b, 2))
print(f"The length of the Hypotenuse is {c}")