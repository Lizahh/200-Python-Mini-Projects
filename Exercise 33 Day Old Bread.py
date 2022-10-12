# -*- coding: utf-8 -*-
"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.


"""

price_of_one_loaf = 3.49
user_input = int(input("Please enter the number of loaves of day old bread you need: "))

regular_price = user_input * price_of_one_loaf
print("Regular price for your purchase: {r:.2f}".format(r=regular_price))

discounted_price = regular_price * 0.6
print("Discount price for your purchase: {r:.2f}".format(r=discounted_price))

total_price = regular_price - discounted_price
print("Total Price: {r:.2f}".format(r=total_price))

