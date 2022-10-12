# -*- coding: utf-8 -*-
"""

In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.

"""

seconds = int(input("Please enter the number of seconds: "))

days = seconds / 86400
seconds = seconds % 86400
hours = seconds / 3600
seconds = seconds % 3600
minutes = seconds / 60
seconds = seconds % 60

print("D:HH:MM:SS ---> {%d}:{%02d}:{%02d}:{%02d}" %(days, hours, minutes, seconds))

12