# -*- coding: utf-8 -*-
"""Day_37.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yshn-P-5a9Fs8UhZQCD_WRO5MkCVSc4b
"""

def reverse(nums):

  start_index = 0
  last_index = len(num)-1

  while last_index > start_index:

    nums[start_index],nums[last_index] = nums[last_index],nums[start_index]

    start_index = start_index + 1
    last_index = last_index - 1

if __name__ == '__name__':

  n =[1,2,3,4]
  reverse(n)
  print(n)

def reverse(nums):

  start_index = 0
  last_index = len(num)-1

  while last_index > start_index:

    nums[start_index],nums[last_index] = nums[last_index],nums[start_index]

    start_index = start_index + 1
    last_index = last_index - 1

if __name__ == '__name__':

  n =[1,2,3,4]
  reverse(n)
  print(n)