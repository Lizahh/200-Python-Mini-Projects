# -*- coding: utf-8 -*-
"""


Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf = sqrt(v_i^2 + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.





"""

from math import sqrt

height = float(input("Please enter the height from which the object is dropped in meters (m). "))

v_i = 0
acc = 9.8
v_f = sqrt(v_i**2 + 2*acc*height)

print("How quickly an object is traveling when it hits the ground is ", v_f)

