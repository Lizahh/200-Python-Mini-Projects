# -*- coding: utf-8 -*-
"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.

"""

flag = True
while(flag == True):
  user_input = input("Please enter name of month:")
  if user_input == 'January' or user_input =='March' or user_input =='May' or user_input =='July' or user_input == 'August' or user_input =='October' or user_input =='December':
    print("{} has {} number of days.".format(user_input, 31))
    flag = False
  elif user_input == 'April' or user_input =='June' or user_input =='September' or user_input =='November':
    print("{} has {} number of days.".format(user_input, 30))
    flag = False
  elif user_input == 'February':
    print("{} has 28 or 29 days.".format(user_input))
    flag = False
  else:
    print("Please enter month name complete e.g. January ... ")

