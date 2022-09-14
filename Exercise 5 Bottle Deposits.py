# -*- coding: utf-8 -*-
"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.




"""

cont_le_liter = int(input("Please enter the number of containers of 1 liter or less:"))
cont_greater_than_liter = int(input("Please enter the number of containers of greater than 1 liter:"))

refund_le_liter = cont_le_liter * 0.10
refund_greater_than_liter = cont_greater_than_liter * 0.25
total_refund = refund_le_liter + refund_greater_than_liter
print("Total refund is = ${r:.2f}".format(r=total_refund))

