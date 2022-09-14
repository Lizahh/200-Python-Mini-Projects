# -*- coding: utf-8 -*-
"""

An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.


"""

widgets = int(input("Please enter number of widgets: "))
gizmos = int(input("Please enter number of gizmos: "))
total_weight = widgets * 75 + gizmos * 112
print("Total weight is: {}".format(total_weight))

