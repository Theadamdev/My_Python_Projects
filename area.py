#Ask about wheter he wants to calculate the area of a triangle , square , rectangle and circle
import math
pi = math.pi
while True:
    shape = str(input("Enter the wanted shape (triangle/square/rectangle/circle) : "))
    if shape == "triangle":
        height = float(input("Enter the height of the base : "))
        base = float(input("Enter the length of the base : "))
        area = (height * base)/2
        print(f"The area of your triangle is {area}")
        break
    elif shape == "square":
        side = float(input("Enter the length of the side of your square : "))
        area = pow(side, 2)
        print(f"The area of your square is {area}")
        break
    elif shape == "rectangle":
        length = float(input("Enter the length of your rectangle: "))
        width = float(input("Enter the width of your rectangle: "))
        area = length * width
        print(f"The area of your rectangle is {area}")
        break
    elif shape == "circle":
        radius = float(input("Enter the radius of your circle: "))
        area = pi * radius
        print(f"The area of your circle is {area}")
        break
    else:
        print("Please enter a valid shape")