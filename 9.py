# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:54:44 2019

@author: reon
"""

a=input('文字列を入力してください　> ')
if a[::-1]==a:
    print('回文です')
else:
    print('回文ではありません')