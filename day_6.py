# -*- coding: utf-8 -*-
"""day 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U3u5-duc8ywwvr7748cZPFUVxc-8I-4X
"""

#Create an empty tuple

empty_tuple = tuple()
print(empty_tuple)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sis = ('kavya', 'sri', 'baby')
print(sis)
bro = ('devi', 'charan', 'surya')
print(bro)


#Join brothers and sisters tuples and assign it to siblings

sis = ('kavya', 'sri', 'baby')

bro = ('devi', 'charan', 'surya')

siblings = sis + bro

print(siblings)

#How many siblings do you have?

len(siblings)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

sis = ('kavya', 'sri', 'baby')
sis = list(sis)
sis.insert(3, 'Dattu')
sis.insert(4, 'sri devi')
sis = tuple(sis)
print (sis)


s = sis + bro
print(s)

#Unpack siblings and parents from family_members


#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('apple','pineapple','waterapple')

vegetables = ('carrot','beetroot','capsicum')

animal =('dog','cat','rat')

food_stuff_tp = fruits + vegetables +  animal

print(food_stuff_tp)


#Change the about food_stuff_tp tuple to a food_stuff_lt list


klu = ('apple', 'pineapple', 'waterapple', 'carrot', 'beetroot', 'capsicum', 'dog', 'cat', 'rat')

aList = list(klu)

print(type(aList))
print(aList)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

food_stuff_lt = ['apple', 'pineapple', 'waterapple', 'carrot', 'beetroot', 'capsicum', 'dog', 'cat', 'rat']

print(food_stuff_lt[ :5: ])

#Slice out the first three items and the last three items from food_staff_lt list

food_stuff_lt = ['apple', 'pineapple', 'waterapple', 'carrot', 'beetroot', 'capsicum', 'dog', 'cat', 'rat']

print(food_stuff_lt[ 3: :3 ])

#Delete the food_staff_tp tuple completely

klu =  ('apple', 'pineapple', 'waterapple', 'carrot', 'beetroot', 'capsicum', 'dog', 'cat', 'rat')
del klu

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')