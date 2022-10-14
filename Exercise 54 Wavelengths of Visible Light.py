# -*- coding: utf-8 -*-
"""
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:
Color Wavelength (nm)
Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750
Write a program that reads awavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.

"""

user_input = int(input("Please enter the wavelength: "))

if user_input == 380 or user_input < 450:
  print("Violet")
elif user_input == 450 or user_input < 495:
  print("Blue")
elif user_input == 495 or user_input < 570:
  print("Green")
elif user_input == 570 or user_input < 590:
  print("Yellow")
elif user_input == 590 or user_input < 620:
  print("Orange")
elif user_input == 620 or user_input <= 750:
  print("Red")
else:
  print("This wavelength is outside of the visible spectrum")

