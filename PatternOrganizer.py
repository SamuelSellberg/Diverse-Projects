# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 01:27:17 2018

@author: Admin
"""

import math


def positioning(num,channels,embedded=True):
    result = [False]*num
    if embedded == True:
        arrangement = patternOrganizer(num,channels)
    else:
        prevArrangement = patternOrganizer(num-2,channels-2)
        arrangement = [0]+prevArrangement+[0]
    rest = 0
    for i in range(len(arrangement)-1):
        result[arrangement[i]+rest] = True
        rest += arrangement[i]+1
    return result


def patternOrganizer(total,dividers):
    blocks = dividers+1
    X = (total-dividers)/blocks
    spacing = [math.floor(X)]*blocks
    even = (blocks%2)==0
    incNum = round((X%1)*blocks)
    if incNum==0:          # Tom för både Even och Uneven                      Testa: 20,6 23,5
        print('Empty')
        return spacing
    if (blocks-incNum)>=incNum:
        major = blocks-incNum
        minor = incNum
        inverted = False
    else:
        major = incNum
        minor = blocks-incNum
        inverted = True
    if even==True:
        if major==minor:          # Halv för Even                              Testa: 20,5
            for i in range(int(blocks/2)):
                spacing[2*i+1] += 1
            print('Half')
            return spacing
        elif minor==1:          # Center för Even (Tar även den inverterade då inverted==True)
            if inverted==False:                                              # Testa: 12,3
                spacing[int(blocks/2)] += 1
                print('Center Offset')
            else:                                                            # Testa: 14,3
                for i in range(blocks):
                    if i!=(blocks/2-1):
                        spacing[i] += 1
                print('Inverted Center Offset')
            return spacing
    elif even==False:
        if minor==1:          # Center för Uneven (Tar även den inverterade då inverted==True)
            if inverted==False:                                              # Testa: 21,6
                spacing[math.floor(blocks/2)] += 1
                print('Center')
            else:                                                            # Testa: 26,6
                for i in range(blocks):
                    if i!=math.floor(blocks/2):
                        spacing[i] += 1
                print('Inverted Center')
            return spacing
        elif minor==(major-1):          # Halv för Uneven (Tar även den inverterade då inverted==True)
            if inverted==False:                                              # Testa: 30,8
                for i in range(math.floor(blocks/2)):
                    spacing[2*i+1] += 1
                print('Minor Half')
            else:                                                            # Testa: 31,8
                for i in range(math.ceil(blocks/2)):
                    spacing[2*i] += 1
                print('Major Half (Inverted)')
            return spacing
    print('Subset')
    subset = patternOrganizer(blocks,minor)
    if inverted==False:  
        travel = subset[0]
        for i in range(len(subset)-1):
            spacing[travel] += 1
            travel += subset[i+1]+1
    else:
        travel = 0
        for i in range(len(subset)):
            for j in range(subset[i]):
                spacing[travel+j] += 1
            travel += subset[i]+1
    return spacing