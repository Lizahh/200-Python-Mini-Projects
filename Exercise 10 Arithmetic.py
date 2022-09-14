# -*- coding: utf-8 -*-
"""
Create a program that reads two integers, a and b, from the user.Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log_10 a
• The result of a^b
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.



"""

import math

a = int(input("Please enter integer a: "))
b = int(input("Please enter integer b: "))

print("The sum of a and b: {}".format(a+b))
print("The difference when b is subtracted from a: {}".format(b-a))
print("The product of a and b: {}".format(a*b))
print("The quotient when a is divided by b: {}".format(a/b))
print("The remainder when a is divided by b: {}".format(a%b))
print("The result of log10 a: {}".format(math.log10(a)))
print("The result of a power b: {}".format(a**b))

