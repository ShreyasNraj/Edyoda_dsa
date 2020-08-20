#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 01:32:50 2020

@author: Shreyu
"""
from collections import deque
n=int(input())
a=list(map(int,input().split()))
k=int(input())
def printMax(a,n,k):
    Q=deque()
    for i in range(k):
        while Q and a[i]>=a[Q[-1]]:
            Q.pop()
        Q.append(i)
    for i in range(k,n):
        print(str(a[Q[0]]),end=' ')
        
        while Q and Q[0]<=i-k:
            Q.popleft()
        
        while Q and a[i]>=a[Q[-1]]:
            Q.pop()
        Q.append(i)
    print(a[Q[0]])
    
printMax(a,n,k)   
    

    
    
    
    
    
