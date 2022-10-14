# -*- coding: utf-8 -*-
"""
The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.

Year Animal
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare
Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.


"""

user_input = int(input("Please enter the year: "))

if user_input % 12 == 8:
  print("Dragon")
elif user_input % 12 == 9:
  print("Snake")
elif user_input % 12 == 10:
  print("Horse")
elif user_input % 12 == 11:
  print("Sheep")
elif user_input % 12 == 0:
  print("Monkey")
elif user_input % 12 == 1:
  print("Rooster")
elif user_input % 12 == 2:
  print("Dog")
elif user_input % 12 == 3:
  print("Pig")
elif user_input % 12 == 4:
  print("Rat")
elif user_input % 12 == 5:
  print("Ox")
elif user_input % 12 == 6:
  print("Tiger")
elif user_input % 12 == 7:
  print("Hare")

