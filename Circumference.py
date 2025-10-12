#Calculate the circumference of a circle
import math
pi = math.pi
while True :
    diameter_radius = str(input("Do you have a radius or a diameter ? "))
    if diameter_radius == "radius" or diameter_radius == "a radius":
        radius = float(input("Enter the radius of the circle : "))
        circumference = 2 * pi * radius
        print(f"The circumference of the circle is : {circumference}")
        break
    elif diameter_radius == "diameter" or diameter_radius == "a diameter":
        diameter = float(input("Enter the diameter of the circle :"))
        circumference = pi * diameter
        print(f"The circumference of the circle is  : {circumference}")
        break
    else:

        print("Please enter a valid answer.")
