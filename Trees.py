#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:03:25 2020

@author: Shreyu
"""
n=int(input())
link=list(map(int,input().split()))
def findHeight():
    depth=[0 for i in range(n)]
    for i in range(n):
        findDepth(link,i,depth)
    ht = depth[0] 
    for i in range(1,n): 
        ht = max(ht, depth[i]) 
  
    return ht 

def findDepth(link,i,depth):
    if depth[i] != 0: 
        return
    if link[i] == -1: 
        depth[i] = 1
        return 
    if depth[link[i]] == 0: 
        findDepth(link, link[i] , depth) 

    depth[i] = depth[link[i]] + 1
ht=findHeight()
print(ht)


