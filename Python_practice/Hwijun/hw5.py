# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:13:20 2020

@author: 9810_
"""

n = int (input("숫자를 입력하세요 : " ))


while 1 :
    
    m = int (input(""))   

    if m == 0 :
        
        print(n)
        
        break
    
    if m < 0 :
        m = abs(m)
        
    if ( m % 2 ) == 0 :
        n = n * m
        #print (n, end = ' ')
        #연산값을 바로 출력
        
    else:
        n = n + m
        #print(n, end = ' ')
        #연산값을 바로 출력
        
        
