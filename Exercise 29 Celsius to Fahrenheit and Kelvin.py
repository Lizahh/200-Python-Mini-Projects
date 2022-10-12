# -*- coding: utf-8 -*-
"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet

"""

import math
C = float(input("Please enter the temperature in degrees Celsius:"))

faren = (C * 9/5) + 32
kelvin = C +  273.15
print("Tempreture in farenheit: {}".format(faren))
print("Tempreture in Kelvin: {}".format(kelvin))

