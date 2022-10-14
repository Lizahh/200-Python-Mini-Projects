# -*- coding: utf-8 -*-
"""
Canada has three national holidays which fall on the same dates each year.
Holiday Date
New year’s day January 1
Canada day July 1
Christmas day December 25
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
Canada has two additional national holidays, Good Friday and Labour Day,
whose dates vary from year to year. There are also numerous provincial and
territorial holidays, some of which have fixed dates, and some of which have
variable dates. We will not consider any of these additional holidays in this
exercise.


"""

month = input("Please enter the name of the month: ")
day = int(input("Please enter the day (like 1 etc.): "))

if month == "January" or month == "january" and day == 1:
  print("Its New year’s day")
elif month == "July" or month == "july" and day == 1:
  print("Its Canada day")
elif month == "December" or month == "december" and day == 25:
  print("Its Christmas day")
else:
  print("Entered month and day do not correspond to a fixed-date holiday.")


