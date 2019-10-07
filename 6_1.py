# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:32:50 2019

@author: reon
"""

for i in range(5):
    x=int(input('数字を入力してください'))
    if x%7==0:
        print('７の倍数です')
    else:
        print('７の倍数ではありません')
    if x%3==0:
        print('３の倍数です')
    else:
        print('３の倍数ではありません')
    if x<0:
        print('負の数です')
    else:
        print('正の数です')