# -*- coding: utf-8 -*-
"""

In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
(MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPGto L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.


"""

mpg = float(input("Please enter the fuel efficieny in miles per gallons: "))
Liter_per_100km = 235.215/mpg

print("Your equivalent fuel efficiency in Canadian units:", Liter_per_100km)

