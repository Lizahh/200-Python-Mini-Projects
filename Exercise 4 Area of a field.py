# -*- coding: utf-8 -*-
"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.


"""


squares_feet_in_acres = 43560
length = float(input("Please enter length of the field:"))
width = float(input("Please enter width of the field:"))
area = length * width / squares_feet_in_acres
print("Area of the room = {} square feet".format(area))

