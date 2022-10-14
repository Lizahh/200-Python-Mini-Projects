# -*- coding: utf-8 -*-
"""
The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:
Magnitude Descriptor
Less than 2.0 Micro
2.0 to less than 3.0 Very minor
3.0 to less than 4.0 Minor
4.0 to less than 5.0 Light
5.0 to less than 6.0 Moderate
6.0 to less than 7.0 Strong
7.0 to less than 8.0 Major
8.0 to less than 10.0 Great
10.0 or more Meteoric
Write a program that reads amagnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.

"""

user_input = float(input("Please enter the magnitude of the earthquake: "))

if user_input < 2.0:
  print("Magnitude of {} earthquake is considered to be a micro earthquake.")

elif user_input >=2.0 and user_input < 3.0:
  print("Magnitude of {} earthquake is considered to be a very minor earthquake.")

elif user_input >=3.0 and user_input < 4.0:
  print("Magnitude of {} earthquake is considered to be a minor earthquake.")

elif user_input >=4.0 and user_input < 5.0:
  print("Magnitude of {} earthquake is considered to be a light earthquake.")

elif user_input >=5.0 and user_input < 6.0:
  print("Magnitude of {} earthquake is considered to be a moderate earthquake.")

elif user_input >=6.0 and user_input < 7.0:
  print("Magnitude of {} earthquake is considered to be a strong earthquake.")

elif user_input >=7.0 and user_input < 8.0:
  print("Magnitude of {} earthquake is considered to be a major earthquake.")

elif user_input >=8.0 and user_input < 10.0:
  print("Magnitude of {} earthquake is considered to be a great earthquake.")

else:
  print("Magnitude of {} earthquake is considered to be a meteroric earthquake.")

