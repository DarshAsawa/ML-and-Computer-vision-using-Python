# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 13:24:56 2020

@author: dasaw
"""

fizzbuzz = int(input("Enter a number: "))
if fizzbuzz % 3==0 and fizzbuzz % 5==0:
    print("fizzbuzz")
elif fizzbuzz % 3==0:
    print("fizz")
    
elif fizzbuzz % 5==0:
    print("buzz")
else:
    print(fizzbuzz)
