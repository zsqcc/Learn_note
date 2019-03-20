# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:36:30 2019

@author: shuquan.zhang
"""
import bisect

def InversePairs(data):
    data.reverse()
    L=[]
    ret=0
    for d in data:
        pos=bisect.bisect_right(L,d)
        L.insert(pos,d)
        ret+=pos
        ret=ret%10000000007
    return ret % 10000000007



InversePairs([1,2,3,4,5,6,7,0])