# -*- coding: utf-8 -*-
"""
It is common for images of a country’s previous leaders, or other individuals of historical
significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in Table 2.1.
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.

Table 2.1 Individuals that appear on Banknotes
Individual  		Amount
George Washington 	$1
Thomas Jefferson 	$2
Abraham Lincoln 	$5
Alexander Hamilton 	$10
Andrew Jackson 		$20
Ulysses S. Grant 	$50
Benjamin Franklin 	$100

While two dollar banknotes are rarely seen in circulation in the United States,
they are legal tender that can be spent just like any other denomination. The
United States has also issued banknotes in denominations of $500, $1,000,
$5,000, and $10,000 for public use. However, high denomination banknotes
have not been printed since 1945 and were officially discontinued in 1969. As
a result, we will not consider them in this exercise.
"""

user_input = int(input("Please enter the denomination of a banknote: "))


# If the frequency is within one Hertz of a value listed in the table in the previous question then report the name of the note
if user_input == 1:
  print("The note of ${} has George Washington on it.".format(user_input))
elif user_input == 2:
  print("The note of ${} has Thomas Jefferson on it.".format(user_input))
elif user_input == 5:
  print("The note of ${} has Abraham Lincoln on it.".format(user_input))
elif user_input == 10:
  print("The note of ${} has Alexander Hamilton on it.".format(user_input))
elif user_input == 20:
  print("The note of ${} has Andrew Jackson on it.".format(user_input))
elif user_input == 50:
  print("The note of ${} has Ulysses S. Grant on it.".format(user_input))
elif user_input == 100:
  print("The note of ${} has Benjamin Franklin on it.".format(user_input))
else:
  note = "No such note exists"

