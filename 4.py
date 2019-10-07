# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:20:43 2019

@author: reon
"""

num1=int(input('借金の総額を入力してください > '))
num2=int(input('ひと月に返済する金額を入力してください　> '))
num3=(num1/num2)
num4=num3//12
print('返済まで%d年かかります'%num4)
num5=int(input('ボーナスから返済する金額を入力してください　> '))
num6=num3-(num1/(num2+num5))
print('返済が%d年早まります'%num6)
year=int(input('返済したい年入力してください　>'))
print((num1-((year-2019)*5000))/(year-2019),'円必要です')