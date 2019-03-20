# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:39:13 2019

@author: cooper
"""
import pandas as pd

#print(pd.MultiIndex(levels=[['a','b'],[1,2],[3,4]],labels=[[0,0,1,1],[0,1,0,1]]))
df_product1=pd.MultiIndex.from_product([['a','b'],['c','d']])
print(df_product1)
df_product2=pd.MultiIndex.from_product([['a','b'],['c','d'],['e','f']])
print(df_product2)