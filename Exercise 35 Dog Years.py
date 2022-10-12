# -*- coding: utf-8 -*-
"""
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number

"""

human_age = int(input('Input a dog age in human years: '))

if human_age < 0:
	print('Age must be positive number')
	
elif human_age <= 2:
	dog_age = human_age * 10.5
else:
	dog_age = 21 + (human_age - 2)*4    # 10.5 * 2 = 21

print('The dog age is {}'.format(dog_age))

2