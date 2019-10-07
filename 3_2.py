# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:56:29 2019

@author: reon
"""

l=[]
c=('')
for i in range(10):
    a=input('整数を入力してください> ')
    b=int(a)
    l.append(b)
    if l[i] < 0 :
        c=('負の数が含まれています')
print(l)
print(c)
print(sum(l))