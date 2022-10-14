# -*- coding: utf-8 -*-
"""
In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average.

"""

user_input = float(input("Please enter the grade point: "))

if user_input >= 4.0:
  print("A+")
elif user_input < 4.0 and user_input >= 3.7:
  print("A-")
elif user_input < 3.7 and user_input >= 3.3:
  print("B+")
elif user_input < 3.3 and user_input >= 3.0:
  print("B")
elif user_input < 3.0 and user_input >= 2.7:
  print("B-")
elif user_input < 2.7 and user_input >= 2.3:
  print("C-")
elif user_input < 2.3 and user_input >= 2.0:
  print("C")
elif user_input < 2.0 and user_input >= 1.7:
  print("C+")
elif user_input < 1.7 and user_input >= 1.3:
  print("D-")
elif user_input < 1.3 and user_input >= 1.0:
  print("D")
else:
  print("F")

