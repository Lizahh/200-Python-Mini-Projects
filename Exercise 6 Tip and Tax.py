# -*- coding: utf-8 -*-
"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.



"""

meal_cost = float(input("Please enter the cost of the meal: "))
tip = meal_cost * 0.18
tax = meal_cost * 0.17
total_cost = meal_cost+ tip +tax
print("Tax Amount: {r:.2f}".format(r=tax))
print("Tip Amount: {r:.2f}".format(r=tip))
print("Total Amount: {r:.2f}".format(r=total_cost))

