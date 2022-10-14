# -*- coding: utf-8 -*-
"""
At a particular company, employees are rated at the end of each year. The rating scale
begins at 0.0, with higher values indicating better performance and resulting in larger
raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
with each rating is shown in the following table. The amount of an employee’s raise
is $2400.00 multiplied by their rating.
Rating Meaning
0.0 Unacceptable performance
0.4 Acceptable performance
0.6 or more Meritorious performance
Write a program that reads a rating from the user and indicates whether the performance
was unacceptable, acceptable or meritorious. The amount of the employee’s
raise should also be reported. Your program should display an appropriate error
message if an invalid rating is entered.

"""

user_input = float(input("Please enter the rating: "))

if user_input == 0.0:
  raise_in_salary = user_input * 2400.00
  print("Unacceptable performance with {} raise in salary!".format(raise_in_salary))
elif user_input == 0.4:
  raise_in_salary = user_input * 2400.00
  print("Acceptable performance with {} raise in salary!".format(raise_in_salary))
elif user_input >= 0.6:
  raise_in_salary = user_input * 2400.00
  print("Meritorious performance with {} raise in salary!".format(raise_in_salary))
else:
  print("Invalid Rating!")

