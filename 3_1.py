# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:20:42 2019

@author: reon
"""

l=[]
for i in range(10):
    a=input('整数を入力してください> ')
    b=int(a)
    l.append(b)
if 5 not in l:
    print('Boo')
print(l)
print(sum(l))