# -*- coding: utf-8 -*-
"""day4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hpoBtqLdHUqZfzLU2L5GPTkDrjwkVJJk
"""

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

s1 = 'thirty'
s2 = 'days'
s3 = 'of'
s4 = 'python'

s5 =s1+s2+s3+s4

print(s5)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
#Declare a variable named company and assign it to an initial value "Coding For All".
#Print the variable company using print().

#Print the length of the company string using len() method and print().
string = "Geeksforgeeks"
print(len(string))

#Change all the characters to uppercase letters using upper() method.
string = "Geeksforgeeks"
print(string.upper())

#Change all the characters to uppercase letters using lower() method.
string = "Geeksforgeeks"
print(string.lower())

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

s1 = 'Coding'
s2 = 'For'
s3 =  "All"

s4 =s1 +' '+ s2 +' '+ s3

print(s4)

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

name = "geeks FOR geeks"
print(name.capitalize())

print("geeks_for_geeks".title())

string = "gEEksFORgeeks"
print(string.swapcase())   
  
string = "surya" 
print(string.swapcase())

#Cut(slice) out the first word of Coding For All string.

s= 'Coding For All'
print(s.split())

print(s[6:].lstrip())

#Replace the word coding in the string 'Coding For All' to Python.

id = 'Coding For All'
k = id.replace('Coding For All','Python')
print(id)
print(k)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

s ='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
k= s.split(',')
print(k)

#What is the character at index 0 in the string Coding For All.

k='Coding For All'
print(k[0])

#What is the last index of the string Coding For All.
k='Coding For All'
print(k[-1])

#What character is at index 10 in "Coding For All" string.
k='Coding For All'
print(k[10])

#Use index to determine the position of the first occurrence of C in Coding For All.

k='Coding For All'
print(k[0])

#Use index to determine the position of the first occurrence of F in Coding For All.

k='Coding For All'
print(k[7])

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
k='Coding For All People'
print(k[19])

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
s = "You cannot end a sentence with because because because is a conjunction"
s.find('because')

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
s = "You cannot end a sentence with because because because is a conjunction"
s.rindex('because')

#Does ''Coding For All' start with a substring Coding?

s ='Coding For All'
print(s.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
s ='Coding For All'
print(s.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
s='   Coding For All      '
s.replace(" ", "")

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

a = "30DaysOfPython"
b = "thirty_days_of_python"
print(a.isidentifier())
print(b.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

L = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
x = '#'.join(L)
print(x)

