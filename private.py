
import os
import random
import sys

class Car:

    def __init__(self):
        self.__companyName = None
        self.__carModel = None
        self.__carColor = None
    def set_company(self,companyName):
        self.__companyName = companyName
    def set_model(self,modelName):
        self.__carModel = modelName
    def set_color(self,color):
        self.__carColor = color
    def carInfoDisplay(self):
        return "Name of Motor Company : {}  \nCar Model : {}  \nCar Color : {} ".format(self.__companyName,
                                                                                     self.__carModel,
                                                                                     self.__carColor)
#carObj = Car("Lexus Motors","RX135","Swan White")
carObj = Car()
carObj.set_company('Lexus Motors')
carObj.set_model('RX-135')
carObj.set_color('Swan White')
print(carObj.carInfoDisplay())
