import random
import os
import sys

pi_tuple = (6,7,13.6,12.5,20)
new_list = list(pi_tuple)
print("Tuple : ",pi_tuple)
print("List : ",new_list)
new_tup = tuple(new_list)
print("The same tuple : ",new_tup)
print("Length of tuple : ",len(new_tup))
print("Minimum of tuple : ",min(new_tup))
print("Maximum of tuple : ",max(new_tup))
