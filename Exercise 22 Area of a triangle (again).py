# -*- coding: utf-8 -*-
"""

In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = sqrt(s × (s − s1) × (s − s2) × (s − s3))

Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.

"""

s1 = int(input("Enter the length of side 1 of the triangle: "))
s2 = int(input("Enter the length of side 2 of the triangle: "))
s3 = int(input("Enter the length of side 3 of the triangle: "))

s = (s1 + s2 + s3) / 2
area  = (s* (s - s1)*(s - s2)*(s - s3))**0.5
print("Area of triangle is: {}".format(area))

3