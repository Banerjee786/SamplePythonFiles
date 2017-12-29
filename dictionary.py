import sys
import random
import os

'''
Dictionary
'''
cars = {"Toyota":"Japan","Ford":"USA","BMW":"Germany","Tata":"India","Audi":"Germany","Bugatti":"Italy","Chevrolet":"USA"}
print(cars['BMW'])
print("Length of dictionary : ",len(cars))
print(cars.keys())
print(cars.values())
del cars['Chevrolet']
print(cars.keys())
print(cars.values())
