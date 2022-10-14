# -*- coding: utf-8 -*-
"""
In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers. When all of the license plates following that pattern had
been used, the format was changed to four numbers followed by three uppercase
letters.
Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate.

"""

plate = input("Please enter the license plate number: ")

if len(plate) == 6:
  if plate[0].isalpha() == True and plate[0:3].isupper() == True and plate[3:6].isnumeric() == True:
    print("Old style license plate")
  else:
    print("Wrong Input!")

elif len(plate) == 7:
  if plate[0].isalpha() == False and plate[0:4].isnumeric() == True and plate[4:7].isalpha() == True:
    print("New style license plate")
  else:
    print("Wrong Input!")

else:
  print("Invalid Input!")