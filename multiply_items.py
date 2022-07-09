# Write a Python program to multiply all the items in a dictionary.

from itertools import product


dictionary = {1:1,2:4,3:9,4:16}

product = 1
for i in (dictionary):
    product *= dictionary[i]

print(product)    