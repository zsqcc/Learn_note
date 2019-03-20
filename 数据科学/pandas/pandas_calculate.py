# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sat Mar  9 21:52:47 2019

@author: cooper
=======
pandasd的基本运算

@author: shuquan.zhang
>>>>>>> 16ec243f861fdf7887d33d702f7fcf649331872a
"""
import pandas as pd
import numpy as np

<<<<<<< HEAD
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
=======
rng=np.random.RandomState(42)
ser=pd.Series(rng.randint(0,10,4))
print(ser)
# 使用dataframe
df=pd.DataFrame(rng.randint(0,10,(3,4)),columns=['a','b','c','d'],index=['A','B','C'])
print(df)
# 返回以e的ser次方
exp=np.exp(ser)
print(exp)
# 做sin运算
print(np.sin(df*np.pi/4))
# 自动对齐索引进行计算
area=pd.Series({'Alaska':1000,'Texas':65422,'california':33223})
pop=pd.Series({'california':3332,'Texas':23455,'New York':3211})
print(pop/area)
print(pop.index | area.index)
# dataframe的加法运算，自动将索引对齐，当两值中有缺失时，结果用NaN代替
A=pd.DataFrame(rng.randint(0,20,(2,2)),columns=list('AB'))
B=pd.DataFrame(rng.randint(0,30,(3,3)),columns=list('BAC'))
print(A+B)
# 使用默认值替换不存在的值
print(A.add(B,fill_value=0))
# 矩阵运算
C=rng.randint(10,size=(3,4))
print(C-C[0])
>>>>>>> 16ec243f861fdf7887d33d702f7fcf649331872a
