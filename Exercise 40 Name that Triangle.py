# -*- coding: utf-8 -*-
"""

A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle

"""

side_1 = int(input("Please enter length of side 1 of triangle: "))
side_2 = int(input("Please enter length of side 2 of triangle: "))
side_3 = int(input("Please enter length of side 3 of triangle: "))

if side_1 == side_2 == side_3:
  print("Its an equilateral triangle")

elif side_1 == side_2 or side_2 == side_3:
  if side_1 > side_2 or side_1 < side_2 or side_1 > side_3 or side_1 < side_3 or side_2 > side_3 or side_2 < side_3:
    print("Its an isosceles triangle")

else:
  print("Its scalene triangle.")

2