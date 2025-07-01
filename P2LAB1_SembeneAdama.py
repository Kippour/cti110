# Adama Junior Sembene
# July 1, 2025
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle based on the user's input for the radius.

import math

# Get the radius from the user
radius = float(input("What is the radius of the circle? "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results with formatting
print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
