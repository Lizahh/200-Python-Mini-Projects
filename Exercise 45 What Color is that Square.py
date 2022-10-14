# -*- coding: utf-8 -*-
"""
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row.
Write a program that reads a position from the user. Use an if statement to determine
if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking.
Exercise

"""

position = input("Please enter the position on the chess board: ")

column = position[0]
row = int(position[1])

if column in 'aceg':    # It means column starts with a black box so now all odd number rows will be black for it. Here we will do modular arithmetic
  if row % 2 == 0:
    print("{} is a white box".format(position))
  else:
    print("{} is a black box".format(position))
else:
    if row % 2 == 0:
      print("{} is a black box".format(position))
    else:
      print("{} is a white box".format(position))

