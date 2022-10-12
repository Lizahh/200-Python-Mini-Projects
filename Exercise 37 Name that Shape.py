# -*- coding: utf-8 -*-
"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.

"""

user_input = int(input("Please enter number of sides of shape:"))
if user_input == 3:
  print("Its a trigon")
elif user_input == 4:
  print("Its a quadrilateral")
elif user_input == 5:
  print("Its a pentagon")
elif user_input == 6:
  print("Its a hexagon")
elif user_input == 7:
  print("Its a heptagon")
elif user_input == 8:
  print("Its a octagon")
elif user_input == 9:
  print("Its a enneagon")
elif user_input == 10:
  print("Its a decagon")
else:
  print("Wrong Input! Please enter number of sides between 3 - 10 (inclusive)")

