# -*- coding: utf-8 -*-
"""
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:
Name Frequency range (Hz)
Radio waves Less than 3 × 109
Microwaves 3 × 109 to less than 3 × 1012
Infrared light 3 × 1012 to less than 4.3 × 1014
Visible light 4.3 × 1014 to less than 7.5 × 1014
Ultraviolet light 7.5 × 1014 to less than 3 × 1017
X-rays 3 × 1017 to less than 3 × 1019
Gamma rays 3 × 1019 or more
Write a program that reads the frequency of the radiation from the user and displays
the appropriate name.

"""

user_input = int(input("Please enter the frequency of the radiation: "))

if user_input < (3 * (10**9)):
  print("Radio waves")
elif user_input == (3 * (10**9)) or user_input < (3 * (10**12)):
  print("Microwaves")
elif user_input == (3 * (10**12)) or user_input < (4.3 * (10**14)):
  print("Infrared light")
elif user_input == (4.3 * (10**14)) or user_input < (7.5 * (10**14)):
  print("Visible light")
elif user_input == (7.5 * (10**14)) or user_input < (3 * (10**17)):
  print("Ultraviolet light")
elif user_input == (3 * (10**17)) or user_input <= (3 * (10**19)):
  print("X-rays")
else:
  print("Gamma Rays")

3 * (10**11)

