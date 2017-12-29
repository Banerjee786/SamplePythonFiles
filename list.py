import sys
import random
import os

''' Lists '''
grocery_list = ["Juice","Bananas","Potatoes","Tomatoes"]
print('Grocery List : ', grocery_list)
print("Grocery First Item : ",grocery_list[0])
grocery_list[0] = "Mango Juice"
print("Grocery First Item : ",grocery_list[0])
print("Grocery List Items : ",grocery_list[1:4])
other_list = ['Car Wash','Cash Withdrawal','Play snooker','Go fishing']
to_do_list = [grocery_list,other_list]
print("To Do List : ",to_do_list)
print("Position[1][3] : ",to_do_list[1][3])
grocery_list.append("Onions")
print('Grocery List After Appending : ', grocery_list)
other_list.insert(1,"Dish Washing")
other_list.remove('Go fishing')
print("New \'To Do List\' : ",to_do_list)
grocery_list.sort()
print("Sorted Grocery List : ",grocery_list)
grocery_list.reverse()
print("Reverse Sorted Grocery List : ",grocery_list)
to_do_list2 = grocery_list + other_list
print("To Do List : ",to_do_list2)
print("Length of To Do List # 2 : ",len(to_do_list2))
print("Length of To Do List : ",len(to_do_list))
print("Minimum of To Do List : ",min(to_do_list2))
print("Maximum of To Do List : ",max(to_do_list2))
