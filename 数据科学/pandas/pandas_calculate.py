# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:52:47 2019

@author: cooper
"""
import pandas as pd
import numpy as np

def calculate():
    npg=np.random.RandomState(42)
    df=pd.DataFrame(npg.randint(0,10,(3,4)),columns=list('abcd'),index=list('ABC'))
    print(df)
    print(df-df.iloc[1])
    print(df-df.loc['A'])
    # 按列计算
    print(df.subtract(df['a'],axis=0))
    halfrow=df.iloc[0,::2]
    print(halfrow)
    print(df-halfrow)
calculate()