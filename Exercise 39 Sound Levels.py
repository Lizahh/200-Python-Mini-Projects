# -*- coding: utf-8 -*-
"""
The following table lists the sound level in decibels for several common noises.

Noise 		Decibel level (dB)
Jackhammer 		130
Gas lawnmower 	106
Alarm clock 	70
Quiet room 	40
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.

"""

user_input = int(input("Please enter the sound level in decibels: "))
if user_input == 130:
  print("Jackhammer")

elif user_input == 106:
  print("Gas lawnmower")

elif user_input == 70:
  print("Alarm clock")

elif user_input == 40:
  print("Quiet room")

elif user_input == 30:
  print("Whispering Nearby")

elif user_input == 20:
  print("Leaves rustling in a tree")

elif user_input <= 10:
  print("Normal Breathing")

elif user_input == 140:
  print("Airplane taking off")

elif user_input > 10 and user_input < 20:
  print("Between Normal Breathing and Leaves rustling in a tree")

elif user_input > 20 and user_input < 30:
  print("Between Leaves rustling in a tree and Whispering Nearby")

elif user_input > 30 and user_input < 40:
  print("Between Whispering Nearby and Quiet room")

elif user_input > 40 and user_input < 70:
  print("Between Alarm clock and Quiet room")

elif user_input > 70 and user_input < 106:
  print("Between Gas lawnmower and Alarm clock")

elif user_input > 106 and user_input < 130:
  print("Between Jackhammer and Gas lawnmower")

elif user_input > 130 and user_input < 140:
  print("Between Jackhammer and firecrackers")

else:
  print("Firecrackers or louder than that")

