# -*- coding: utf-8 -*-
"""
A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
c are constants, and a is non-zero. The roots of a quadratic function can be found
by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
the quadratic formula, shown below:
root = −b ± √ b2 − 4ac / 2a
The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real roots.
If the discriminant is 0, then the equation has one real root. Otherwise the equation
has two real roots, and the expression must be evaluated twice, once using a plus
sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function.Your program
should begin by prompting the user for the values of a, b and c. Then it should display
a message indicating the number of real roots, along with the values of the real roots
(if any).

"""

import cmath
a = float(input("Please enter the value of a: "))
b = float(input("Please enter the value of b: "))
c = float(input("Please enter the value of c: "))

deter = b**2 - 4 * a * c

root1 = (-b- cmath.sqrt(deter))/(2*a)
root2 = (-b+ cmath.sqrt(deter))/(2*a)

if deter < 0:
  print("Quadratic equation does not have any real roots.")
elif deter == 0:
  print("Quadratic equation has one real root that is {}.".format(root1))
else:
  print("Quadratic equation has two real roots and the expression must be evaluated twice, once using a plus sign, and once using a minus sign, when computing the numerator.")
  print("The roots are {} and {}.".format(root1, root2))

