# -*- coding: utf-8 -*-
"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.


"""

feet = float(input("Please enter your number of feet: "))

inches = feet*12
yards = feet/3
miles = feet/5280

print("feet to inches: ", inches)
print("feet to yards: ", yards)
print("feet to miles: ", miles)

