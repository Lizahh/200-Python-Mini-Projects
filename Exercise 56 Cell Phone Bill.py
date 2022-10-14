# -*- coding: utf-8 -*-
"""particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.
"""

min = int(input("Please enter the number of minutes used in a month: "))
msg = int(input("Please enter the number of messages used in a month: "))

base_charges = 15
additional_min_charges = 0.25
additional_msg_charges = 0.15
call_center_charges = 0.44
sales_tax = 0.5
if min <= 50 and msg <= 50:
  tax = (base_charges + call_center_charges) * sales_tax
  bill = base_charges + call_center_charges + tax
  print("Base Charges: {} ".format(base_charges))
  print("Call center charges: {}".format(call_center_charges))
  print("Sales tax: {}".format(sales_tax))
  print("Total Bill: {r:.2f} ".format(r=bill))

elif min > 50 and msg <= 50:
  additional_min = (min - 50) * additional_min_charges
  tax = (base_charges + additional_min + call_center_charges) * sales_tax
  bill = base_charges + additional_min + call_center_charges + tax
  print("Base Charges: {} ".format(base_charges))
  print("Additional minutes charges: {} ".format(additional_min))
  print("Call center charges: {}".format(call_center_charges))
  print("Sales tax: {}".format(sales_tax))
  print("Total Bill: {r:.2f} ".format(r=bill))

elif min <= 50 and msg > 50:
  additional_msgs = (msg - 50) * additional_msg_charges
  tax = (base_charges + additional_msgs + call_center_charges) * sales_tax
  bill = base_charges + additional_msgs + call_center_charges + tax
  print("Base Charges: {} ".format(base_charges))
  print("Additional messages charges: {} ".format(additional_msgs))
  print("Call center charges: {}".format(call_center_charges))
  print("Sales tax: {}".format(sales_tax))
  print("Total Bill: {r:.2f} ".format(r=bill))

elif min > 50 and msg > 50:
  additional_msgs = (msg - 50) * additional_msg_charges
  additional_min = (min - 50) * additional_min_charges
  tax = (base_charges + additional_msgs + additional_min + call_center_charges) * sales_tax
  bill = base_charges + additional_msgs + additional_min + call_center_charges + tax
  print("Base Charges: {} ".format(base_charges))
  print("Additional minutes charges: {} ".format(additional_min))
  print("Additional messages charges: {} ".format(additional_msgs))
  print("Call center charges: {}".format(call_center_charges))
  print("Sales tax: {}".format(sales_tax))
  print("Total Bill: {r:.2f} ".format(r=bill))

else:
  print("Invalid Input")