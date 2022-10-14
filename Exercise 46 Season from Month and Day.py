# -*- coding: utf-8 -*-
"""
The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:
Season First day
Spring March 20
Summer June 21
Fall September 22
Winter December 21

Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.



"""

month = input("Please enter the month name: ")
day = int(input("Please enter the day (e.g. 1 etc. ): "))

if month == 'January' or month == 'February' or month == 'january' or month == 'february' :
  print("Season is Winter!")
elif month == 'March' or month == 'march':
  if day < 20:
    print("Season is Winter!")
  else:
    print("Season is Spring!")
elif month == 'April' or month == 'May' or month == 'april' or month == 'may':
  print("Season is Spring!")
elif month == 'June' or month == 'june':
  if day < 21:
    print("Season is Spring!")
  else:
    print("Season is Summer!")
elif month == 'July' or month == 'August' or month == 'july' or month == 'august':
  print("Season is Summer!")
elif month == 'September':
  if day < 22:
    print("Season is Summer!")
  else:
    print("Season is Fall!")
elif month == 'October' or month == 'November' or month == 'october' or month == 'november':
  print("Season is Fall!")
elif month == 'December' or month == 'december':
  if day < 21:
    print("Season is Fall!")
  else:
    print("Season is Winter!")

