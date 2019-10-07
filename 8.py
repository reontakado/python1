# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:22:58 2019

@author: reon
"""
import sys
x=int(input('番号を入力してください'))
if x%4==0:
    print('４の倍数です')
    sys.exit()
if x%2==0:
    print('偶数です')
else:
    print('奇数です')