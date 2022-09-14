# -*- coding: utf-8 -*-
"""

Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.






"""

amount = int(input("Please enter amount of money deposited into the account: "))
amount_after_year_1 = amount + (amount * 0.4)
amount_after_year_2 = amount_after_year_1 + (amount_after_year_1 * 0.4)
amount_after_year_3 = amount_after_year_2 + (amount_after_year_2 * 0.4)

print("Amount after first year is: {r:.2f}".format(r=amount_after_year_1))
print("Amount after second year is: {r:.2f}".format(r=amount_after_year_2))
print("Amount after thrid year is: {r:.2f}".format(r=amount_after_year_3))

