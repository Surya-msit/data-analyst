# -*- coding: utf-8 -*-
"""day_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kKD6oW1nBbzQOeDtbLq1ncgEM92ofDG_
"""

#Iterate 0 to 10 using for loop, do the same using while loop.

#for i in range(10):
  #print(i)

i = 0
while i < 10:
    print (i)
    i = i + 1

#Iterate 10 to 0 using for loop, do the same using while loop.

#for i in range(10, 0, -1):
 #   print(i)

i = 0
while i > 10:
    print (i)
    i = i - 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

row = int(input('enter the number :'))
for i in range(0,row):
  for j in range(0, i+1):
    print("* ", end =" ")
  print()

n = int(input("Enter the number of rows"))  
# outer loop to handle number of rows  
for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
  
        # ending line after each row  
        print()

n = int(input("enter the number : "))
# Loop through rows
for i in range(n):
    
    # Loop to print pattern
    for j in range(n):
        print('#' , end=' ')
    print()

num = int(input("Enter the number :"))

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#Use for loop to iterate from 0 to 100 and print only even numbers

i = int(input())

for i in range(100):
  if i%2 ==0:

    print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers

i = int(input())

for i in range(100):
  if i%2 !=0:

    print(i)

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.

# Sum of natural numbers up to num

num = int(input("Please enter the number: "))

sum = 0

for value in range(1, num + 1):
    sum = sum + value
    
print(sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

num = int(input("Please enter the number: "))

sum = 0

for value in range(1, num + 1):
    sum = sum + value
    
print(sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

minimum = int(input(" Please Enter the Minimum Value : ")) 
maximum = int(input(" Please Enter the Maximum Value : "))

even_total = 0
odd_total = 0
 
for number in range(minimum, maximum + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, even_total))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, odd_total))

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.


list1 = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(list1) - 1, -1, -1):
    print(list1[i], end=' ')