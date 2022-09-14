# -*- coding: utf-8 -*-
"""

Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.



"""

feet = float(input("Please enter your height in number of feet: "))
inch = float(input("Please enter your height in number of inches: "))

height_in_cm = ((feet*12) + inch)*2.54

print("Your height in centimeters is: ", height_in_cm)

