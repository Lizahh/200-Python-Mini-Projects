# -*- coding: utf-8 -*-
"""

The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.





"""

from math import pi

radius = float(input("Please enter radius of the cylinder: "))
height = float(input("Please enter height of the cylinder: "))

cylinder_area = pi*radius*radius*height

print("Area of cylinder:{r:.1f} ".format(r=cylinder_area))

