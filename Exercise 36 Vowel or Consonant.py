# -*- coding: utf-8 -*-
"""

In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.

"""

user_input = input("Please enter a letter:")
if user_input in 'aeiou':
  print("Its a vowel")
if user_input == 'y':
  print("Sometimes y is a vowel, and sometimes y is a consonant")
else:
  print("Its a consonant")

