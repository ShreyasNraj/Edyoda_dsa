#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:55:34 2020

@author: Shreyu

"""

def error_check(inp):
    open_braces = ["[","{","("] 
    close_braces = ["]","}",")"] 
    stack = [] 
    Dict ={ ')':'(', '}':'{', ']':'['} 
    a = b = c = 0
    for i in inp: 
        if i in open_braces: 
            stack.append(i) 
        elif i in close_braces: 
            pos = close_braces.index(i) 
            if ((len(stack) > 0) and (open_braces[pos] == stack[len(stack)-1])): 
                stack.pop() 
    if len(stack) == 0: 
        return "Success"
    else:
        if inp[0]  in close_braces: 
            print(1) 
        else:
            for i in range(0, len(inp)):
                if inp[i].isalpha():
                    continue
                if inp[i] in open_braces: 
                    stack.append(inp[i]) 
                    k = i + 1
                else:
                    if len(stack)== 0 and (inp[i] in close_braces): 
                        print(i + 1) 
                        c = 1
                        break
                    else:
                        if Dict[inp[i]]== stack[len(stack)-1]: 
                            stack.pop() 
                        else: 
                            print(i + 1) 
                            a = 1
                            break
    if len(stack)== 0 and c == 0: 
        print(0) 
    if a == 0 and b == 0 and c == 0: 
        print(k) 


