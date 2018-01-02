import os
import random
import sys

class Animal:
    '''
    Constructor below :
    '''
    def __init__(self):
        self.name = None
        self.height = None
        self.weight = None
    '''
    #Another way of defining Constructor
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    '''
    def Name(self,animalName):
        self.name = animalName
    def Height(self,animalHeight):
        self.height = animalHeight
    def Weight(self,animalWeight):
        self.weight = animalWeight
    def displayInfo(self):
        return "{} is {} cm tall and weighs {} kgs".format(self.name,self.height,self.weight)
animalObj = Animal()
# animalObj = Animal('Cheetah','120','145') In case constructor contains arguments
animalObj.name = 'Leopard'
animalObj.height = '125'
animalObj.weight = '85'
print(animalObj.displayInfo())
