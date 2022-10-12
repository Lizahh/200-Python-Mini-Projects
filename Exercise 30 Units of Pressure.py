# -*- coding: utf-8 -*-
"""
In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.


"""

import math
p = float(input("Please enter the pressure in kilopascals:"))

pounds_per_square_inch = p/6.895
millimeters_of_mercury = p * 7.501
millimeters_of_atmospheres = p / 101.325

print("Equivalent pressure in pounds per square inch: {}".format(pounds_per_square_inch))
print("Equivalent pressure in millimeters of mercury: {}".format(millimeters_of_mercury))
print("Equivalent pressure in millimeters of atmospheres.: {}".format(millimeters_of_atmospheres))

