# -*- coding: utf-8 -*-
"""
reate a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.

"""

days = int(input("Please enter the number of days: "))
hours = int(input("Please enter the number of hours: "))
minutes = int(input("Please enter the number of minutes: "))
seconds = int(input("Please enter the number of seconds: "))

total_seconds = (86400*days) + (3600*hours) + (60*minutes) + seconds

print("Total number of seconds represented by this duration are: {}".format(total_seconds))

