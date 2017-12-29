import os
import sys
import random

'''
if...else elif
'''
age = 30
if age >= 21:
    print("You are old enough to drive a tractor trailer",end=" ")
    print("and a car too !")
elif age >= 16:
    print("You are old enough to drive a car")
else:
    print("You are not permitted to drive")

'''
For...loop
'''
for x in range(5,10):
    print(x,end=" ")
print('\n')

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for i in range(0,3):
    for j in range(0,3):
        print(num_list[i][j],'\t',end=" ")
    print()


'''
While...loop
'''
print("Printing Random Numbers from 1 to 10")
rand_num = random.randrange(0,10)
while(rand_num != 7):
    print(rand_num)
    rand_num = random.randrange(0,10)
