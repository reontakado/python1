# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:09:33 2019

@author: reon
"""

a=[1,4,9,16,25,36,49,64,81,100]
b=[]
for i in range(10):
    if a[i]%2==0:
        b.append(a[i])
print(b)