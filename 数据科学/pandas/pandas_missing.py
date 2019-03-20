# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:16:21 2019
实际数据往往不是干净整洁的，很多数据集有数据缺失的情况，这时候需要处理缺失值
处理缺失值存在两种主流方法：标签值和掩码
标签值：可能是具体数据或极少出现的形式，或者全局值(NaN)
掩码：掩码可能为一个与原数组维度相同的布尔型数组，也可能是一个比特(0/1)表示缺失值
优缺点：标签值可能增加计算逻辑，掩码带来存储与计算的负担
@author: shuquan.zhang
"""
import numpy as np
import pandas as pd

def pandas_missing():
    # pandas的缺失值有None、NaN
    # python对象的缺失值，使用None
    vals1=np.array([1,None,3,4])
    print(vals1)
    print(vals1.dtype)
    # python对象，对数据的操作在python层面，因而比原生类型数组消耗资源
    # 以下爱代码需要在ipython中使用
#    for tp in ['object','int']:
#        print("dtype =",tp)
#        %timeit np.arange(1E6,dtype=tp).sum()
#        print()
    # python中未定义包含None的数组进行累加等操作
#    vals1.sum()
    # 使用NaN,NaN是一种特殊的浮点数，NaN会将与之交互的数据同化
    vals2=np.array([1,np.nan,3,4])
    print(vals2)
    print(vals2.dtype)
    print(vals2.sum())
    # 使用忽略缺失值的计算函数
    print(np.nansum(vals2))
    # pandas中，没有标签值的数据类型，自动转化为NA
    x=pd.Series(range(3),dtype=int)
    print(x)
    x[0]=None
    print(x)
    # 对缺失值的处理
    data=pd.Series([1,np.nan,'hello',None])
    # 判断是否为缺失值  -->dataframe也适用
    print(data.isnull())
    print(data.notnull())
    print(data[data.notnull()])
    print(data.dropna())
    # dataframe的剔除,可以行或列的剔除
    df=pd.DataFrame([[np.nan,np.nan,0],[2,np.nan,4],[np.nan,2,4]])
    print(df.dropna())
    print(df.dropna(axis='columns'))
    # thresh进一步制定剔除规则
    print(df.dropna(axis='rows',thresh=2))
    print(df.fillna(0))
    # 填充方式可以分为向前 向后填充，不过此种方式可能造成部分值无前值或后值填充
    print(df.fillna(method='ffill'))
    print(df.fillna(method='bfill'))
    # axis=1表示从左往右，axis=0表示从上到下
    print(df.fillna(method='ffill',axis=1))
    
    
    
    
        

    
    

pandas_missing()