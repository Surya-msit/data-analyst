# -*- coding: utf-8 -*-
"""day_20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11fIRgOhTlt852D9yYWljBtfh1wLIL0i8
"""

#Module

"""Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
"""

def greeting(name):
  print("Hello, " + name)

import mymodule

mymodule.greeting("Jonathan")



import mymodule

mymodule.greeting("Jonathan")



person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)

