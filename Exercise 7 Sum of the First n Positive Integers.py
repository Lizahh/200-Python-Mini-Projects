# -*- coding: utf-8 -*-
"""

Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) / 2




"""

input_int = int(input("Please enter an integer: "))
summation = int(((input_int) * (input_int + 1))/2)
print("Sum of the first {} integers from 1 to {} is: {}".format(input_int, input_int, summation))

