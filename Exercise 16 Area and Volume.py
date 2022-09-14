# -*- coding: utf-8 -*-
"""
Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr^2. The
volume of a sphere is computed using the formula volume = (4/3)πr^3.





"""

from math import pi

radius = float(input("Please enter radius: "))

circle_area = pi*radius*radius
sphere_area = (4/3)*pi*(radius**3)

print("Area of circle: ", circle_area)
print("Area of sphere: ", sphere_area)

