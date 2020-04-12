# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:26:49 2020

@author: dasaw
"""
result=[]
l=[]
m=[]

size=int(input("Enter the size of list: "))
for i in range(0,size):
    number=int(input("Enter a number for list: "))
    l.append(number)

print("The list formed is: ", l)

#reversing the list with the use of slicing technique..
m=l[::-1]

print("\n Reverse list is: ", m)

#addition of list to its reverse list...
for i in range(0,size):
    result.append(l[i]+m[i])

print("\nThe result list is: ", result)
