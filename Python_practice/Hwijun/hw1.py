# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:28:52 2020

@author: 9810_
"""
from fractions import Fraction

x1 = int(input('x1 : '))
y1 = int(input('y1 : '))

x2 = int(input('x2 : '))
y2 = int(input('y2 : '))


num1 = float(x1/y1)
num2 = float(x2/y2)
num3 = float ((x1/y1) + (x2/y2))


print (Fraction(num1), '+', Fraction(num2), '=', Fraction(num3))