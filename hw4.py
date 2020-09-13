# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:25:58 2020

@author: 9810_
"""
import numpy as np

n = int(input("행 : "))
m = int(input("열 : "))

list1 = np.arange(n*m).reshape((n,m))

a = int(input("재배열 하고 싶은 행의 크기 : "))
x = int(input("재배열 하고 싶은 열의 크기 : "))

z = n*m
w = a*x

while z % w == 0 :
    w = w + 1


list2 = np.arange(w).reshape((a,x))

list3 = np.where(list2 >= z, 0, list2) # 요소가 z 보다 크면 0으로 반환

  
print ("원래 배열 : ", list1)
print ("")
print ("재배열 : ", list3)






        


