#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 06:07:40 2020

@author: Shreyu
"""

from collections import deque
s,n=list(map(int,input().split()))
a=[]
p=[]
for i in range(n):
    ai,pi=list(map(int,input().split()))
    a.append(ai)
    p.append(pi)
def process(s,n,a,p):
    buffer = deque(maxlen=s)
    start_times = [None] * n
    for i in range(n):
        while buffer and buffer[0] <= a[i]:
            buffer.popleft()
        if len(buffer) >= s:
            start_times[i] = -1
        else:
            start_times[i] = max(a[i], buffer[-1] if buffer else 0)
            buffer.append(start_times[i] + p[i])
    for i in range(len(start_times)):
        print(start_times[i])

process(s,n,a,p)

