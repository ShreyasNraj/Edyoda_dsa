#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:42:02 2020

@author: Shreyu
"""
q=int(input())
result=[]
maxx=0
flag=0
stack=[]
def maxi():
        m=stack[0]
        for i in range(1,len(stack)):
            if stack[i]>m:
                m=stack[i]
        return m
for i in range(q):
    i=input().split()
    if 'push' in i:
        stack.append(int(i[1]))
        if int(i[1])>maxx:
            maxx=int(i[1])
    elif 'pop'in i:
        ele=stack.pop()
        if ele==maxx:
            flag=1
    elif 'max' in i:
        if flag:
            maxx=maxi()
        result.append(maxx)
for i in range(len(result)):
    print(result[i])