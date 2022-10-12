# -*- coding: utf-8 -*-
"""
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
"""

four_digits = input("Please enter 4 digit number:")

first = int(four_digits[0])
second = int(four_digits[1])
third = int(four_digits[2])
forth = int(four_digits[3])

summation = first + second + third + forth

print("The sum of the digits in the number: {}".format(summation))

