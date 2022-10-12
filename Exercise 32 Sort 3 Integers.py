# -*- coding: utf-8 -*-
"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.

"""

first = int(input("Please enter first integer:"))
second = int(input("Please enter second integer:"))
third = int(input("Please enter third integer:"))

max_number = max(first, second)
max_number = max(max_number, third)
min_number = min(first, second)
min_number = min(min_number, third)
middle_number = (first+second+third)-(max_number + min_number)

print("Maximum number:{}".format(max_number))
print("Minimum number:{}".format(min_number))
print("Middle number:{}".format(middle_number))

