# -*- coding: utf-8 -*-
"""
At a particular university, letter grades are mapped to grade points in the following
manner:
Letter Grade points
A+ 4.0
A 4.0
A− 3.7
B+ 3.3
B 3.0
B− 2.7
C+ 2.3
C 2.0
C− 1.7
D+ 1.3
D 1.0
F 0
Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.

"""

user_input = input("Please enter the letter grade: ")
if user_input == 'A+' or user_input == 'A':
  print("Grade point is 4.0")
elif user_input == 'A-':
  print("Grade point is 3.7")
elif user_input == 'B+':
  print("Grade point is 3.3")
elif user_input == 'B':
  print("Grade point is 3.0")
elif user_input == 'B-':
  print("Grade point is 2.7")
elif user_input == 'C+':
  print("Grade point is 2.3")
elif user_input == 'C':
  print("Grade point is 2.0")
elif user_input == 'C-':
  print("Grade point is 1.7")
elif user_input == 'D+':
  print("Grade point is 1.3")
elif user_input == 'D':
  print("Grade point is 1.0")
elif user_input == 'F':
  print("Grade point is 0")
else:
  print("Invalid letter grade!")

