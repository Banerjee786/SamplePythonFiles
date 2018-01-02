import random
import os
import sys

'''
Creating a file and adding information
'''
open_file = open("sampfile.txt","wb")
print("File Name : ",open_file.name)
print("File Mode : ",open_file.mode)
open_file.write(bytes("Welcome to Python Programming","utf-8"))
open_file.write(bytes("\t","utf-8"))
open_file.write(bytes("An object-oriented approach to real-world problems","utf-8"))
open_file.close()

'''
Reading from a File
'''
open_file = open("sampfile.txt","r+")
text_in_file = open_file.read()
print("Contents of the File : \'",open_file.name,"\' is : \'",text_in_file,"\'")
open_file.close()

'''
Deleting a file using os module
'''
os.remove("sampfile.txt")
